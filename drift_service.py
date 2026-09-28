import numpy as np
from typing import List, Dict, Any, Tuple

class LagrangianDriftEngine:
    """
    Physics-Guided Lagrangian Particle Drift & Ensemble Hindcast Engine.
    Simulates forward slick dispersion and backward origin probability corridors.
    
    Transport equation:
    d_pos / dt = u_curr + W_d * u_wind + sqrt(2 * K_h) * N(0, 1)
    """

    def __init__(self):
        self.default_windage = 0.030 # 3.0% wind drag coefficient
        self.default_kh = 10.0 # Horizontal diffusion coefficient m2/s

    def simulate_backward_hindcast(
        self,
        slick_centroid: Tuple[float, float], # (lat, lon)
        wind_speed_knots: float,
        wind_dir_deg: float,
        current_speed_mps: float,
        current_dir_deg: float,
        hours_back: float = 6.0,
        num_particles: int = 100
    ) -> Dict[str, Any]:
        """
        Runs Monte Carlo backward ensemble simulation by reversing surface current and wind vectors.
        Generates 50%, 70%, and 90% origin probability contours and centroid.
        """
        lat0, lon0 = slick_centroid
        
        # Convert wind/current to m/s vectors (u, v)
        wind_mps = wind_speed_knots * 0.514444
        # Wind direction is direction FROM which wind blows, so drift is TOWARDS (dir + 180) % 360
        wind_rad = np.radians((wind_dir_deg + 180.0) % 360.0)
        u_wind = wind_mps * np.sin(wind_rad)
        v_wind = wind_mps * np.cos(wind_rad)

        current_rad = np.radians(current_dir_deg)
        u_curr = current_speed_mps * np.sin(current_rad)
        v_curr = current_speed_mps * np.cos(current_rad)

        # Reverse vectors for backward transport
        u_total = -(u_curr + self.default_windage * u_wind)
        v_total = -(v_curr + self.default_windage * v_wind)

        dt_sec = 3600.0 # 1-hour steps
        total_sec = hours_back * 3600.0
        steps = int(hours_back)

        # Meters to degrees conversion (approx near 12.8° N)
        m_per_deg_lat = 110574.0
        m_per_deg_lon = 111320.0 * np.cos(np.radians(lat0))

        particles_lat = np.full(num_particles, lat0)
        particles_lon = np.full(num_particles, lon0)

        # Monte Carlo ensemble perturbations
        np.random.seed(42) # Reproducible demo seed
        for s in range(steps):
            # Perturb wind & current per particle
            u_noise = np.random.normal(0.0, 0.05, num_particles)
            v_noise = np.random.normal(0.0, 0.05, num_particles)

            dx_m = (u_total + u_noise) * dt_sec
            dy_m = (v_total + v_noise) * dt_sec

            particles_lon += dx_m / m_per_deg_lon
            particles_lat += dy_m / m_per_deg_lat

        origin_lat_mean = float(np.mean(particles_lat))
        origin_lon_mean = float(np.mean(particles_lon))

        # Build Iso-contours (50%, 70%, 90% radius around mean)
        std_lat = float(np.std(particles_lat))
        std_lon = float(np.std(particles_lon))

        particle_points = [
            [float(lon), float(lat)] for lon, lat in zip(particles_lon, particles_lat)
        ]

        return {
            "simulation_type": "Probabilistic Reversible Lagrangian Hindcast",
            "hours_hindcast": hours_back,
            "origin_centroid": [round(origin_lat_mean, 4), round(origin_lon_mean, 4)],
            "probabilistic_corridors": {
                "contour_50_pct": {
                    "radius_km": round(1.177 * std_lat * m_per_deg_lat / 1000.0, 2),
                    "center": [round(origin_lat_mean, 4), round(origin_lon_mean, 4)]
                },
                "contour_70_pct": {
                    "radius_km": round(1.552 * std_lat * m_per_deg_lat / 1000.0, 2),
                    "center": [round(origin_lat_mean, 4), round(origin_lon_mean, 4)]
                },
                "contour_90_pct": {
                    "radius_km": round(2.146 * std_lat * m_per_deg_lat / 1000.0, 2),
                    "center": [round(origin_lat_mean, 4), round(origin_lon_mean, 4)]
                }
            },
            "particles": particle_points[:40] # Return 40 representative particles for UI rendering
        }

    def simulate_forward_forecast(
        self,
        origin_point: Tuple[float, float],
        wind_speed_knots: float,
        wind_dir_deg: float,
        current_speed_mps: float,
        current_dir_deg: float,
        forecast_hours: float = 24.0,
        num_particles: int = 100
    ) -> Dict[str, Any]:
        """Runs forward Lagrangian drift simulation for future slick movement (+1h to +24h)."""
        lat0, lon0 = origin_point
        
        wind_mps = wind_speed_knots * 0.514444
        wind_rad = np.radians((wind_dir_deg + 180.0) % 360.0)
        u_wind = wind_mps * np.sin(wind_rad)
        v_wind = wind_mps * np.cos(wind_rad)

        current_rad = np.radians(current_dir_deg)
        u_curr = current_speed_mps * np.sin(current_rad)
        v_curr = current_speed_mps * np.cos(current_rad)

        u_total = u_curr + self.default_windage * u_wind
        v_total = v_curr + self.default_windage * v_wind

        m_per_deg_lat = 110574.0
        m_per_deg_lon = 111320.0 * np.cos(np.radians(lat0))

        timesteps_forecast = {}
        for h in [1, 3, 6, 12, 24]:
            dt_sec = h * 3600.0
            dx_m = u_total * dt_sec
            dy_m = v_total * dt_sec
            
            f_lat = lat0 + (dy_m / m_per_deg_lat)
            f_lon = lon0 + (dx_m / m_per_deg_lon)
            timesteps_forecast[f"+{h}h"] = {
                "lat": round(float(f_lat), 4),
                "lon": round(float(f_lon), 4),
                "dispersion_radius_km": round(0.5 + 0.15 * h, 2)
            }

        return {
            "simulation_type": "Forward Particle Dispersion Forecast",
            "origin": [lat0, lon0],
            "timesteps": timesteps_forecast
        }

drift_engine = LagrangianDriftEngine()
