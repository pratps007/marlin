from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Tuple

class AISPositionPoint(BaseModel):
    timestamp: str
    lat: float
    lon: float
    sog: float = Field(..., description="Speed over ground in knots")
    cog: float = Field(..., description="Course over ground in degrees")
    heading: float = Field(..., description="Vessel heading in degrees")
    is_gap_point: bool = False

class VesselTrackResponse(BaseModel):
    mmsi: str
    name: str
    vessel_type: str
    flag: str
    total_positions: int
    track: List[AISPositionPoint]

class AISAnomalyItem(BaseModel):
    anomaly_type: str = Field(..., description="e.g. Impossible Speed, Position Jump, Blackout Gap, Heading Mismatch")
    severity: str = Field(..., description="HIGH, MEDIUM, LOW")
    timestamp_range: str
    details: str

class CandidateVesselResponse(BaseModel):
    mmsi: str
    name: str
    type: str
    flag: str
    length_m: float
    width_m: float
    distance_to_centroid_km: float
    time_compatibility_pct: float
    trajectory_fit_pct: float
    counterfactual_fit_pct: float
    ais_reliability: str = Field(..., description="Reliable, Incomplete, Suspicious, Potentially Manipulated, Insufficient Data")
    investigation_priority: str = Field(..., description="HIGH, MEDIUM, LOW")
    has_ais_gap: bool
    gap_duration_hrs: Optional[float] = None
    is_unmatched_satellite_target: bool = False
    anomalies: List[AISAnomalyItem] = []

class CandidateFilterRequest(BaseModel):
    incident_id: str = "MARLIN-X-DEMO-001"
    max_distance_km: float = 50.0
    time_window_hours: float = 12.0
    min_reliability: Optional[str] = None
