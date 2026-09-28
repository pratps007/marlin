from pydantic import BaseModel, Field
from typing import List, Dict, Tuple, Any

class BackwardDriftRequest(BaseModel):
    slick_centroid: Tuple[float, float] = (12.85, 74.22)
    wind_speed_knots: float = 12.5
    wind_dir_deg: float = 240.0
    current_speed_mps: float = 0.45
    current_dir_deg: float = 115.0
    hours_back: float = 6.0
    num_particles: int = 100

class ForwardDriftRequest(BaseModel):
    origin_point: Tuple[float, float] = (12.80, 74.16)
    wind_speed_knots: float = 12.5
    wind_dir_deg: float = 240.0
    current_speed_mps: float = 0.45
    current_dir_deg: float = 115.0
    forecast_hours: float = 24.0

class ContourItem(BaseModel):
    radius_km: float
    center: Tuple[float, float]

class ProbabilisticCorridors(BaseModel):
    contour_50_pct: ContourItem
    contour_70_pct: ContourItem
    contour_90_pct: ContourItem

class BackwardDriftResponse(BaseModel):
    simulation_type: str
    hours_hindcast: float
    origin_centroid: Tuple[float, float]
    probabilistic_corridors: ProbabilisticCorridors
    particles: List[Tuple[float, float]]

class ForwardDriftResponse(BaseModel):
    simulation_type: str
    origin: Tuple[float, float]
    timesteps: Dict[str, Any]
