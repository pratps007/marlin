from pydantic import BaseModel, Field
from typing import List, Dict, Tuple, Any

class CounterfactualRequest(BaseModel):
    mmsi: str = "413291000"
    vessel_release_pos: Tuple[float, float] = (12.80, 74.16)
    vessel_release_time: str = "2026-09-28 03:30 UTC"

class CounterfactualMetrics(BaseModel):
    centroid_distance_delta_km: float
    spatial_iou_overlap_pct: float
    orientation_delta_deg: float
    area_ratio: float
    particle_density_cross_corr: float

class CounterfactualResponse(BaseModel):
    mmsi: str
    candidate_release_position: Tuple[float, float]
    candidate_release_time: str
    observed_slick_centroid: Tuple[float, float]
    physical_compatibility_score_pct: float
    metrics: CounterfactualMetrics
    scientific_label: str
    interpretation: str
