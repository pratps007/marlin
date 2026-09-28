from pydantic import BaseModel, Field
from typing import Dict, List, Tuple, Optional, Any

class SlickGeometryResponse(BaseModel):
    area_sqkm: float = Field(..., description="Slick surface area in square kilometers")
    perimeter_km: float = Field(..., description="Slick perimeter in kilometers")
    centroid: Tuple[float, float] = Field(..., description="Slick centroid [latitude, longitude]")
    length_km: float = Field(..., description="Major axis length in kilometers")
    width_km: float = Field(..., description="Minor axis width in kilometers")
    orientation_deg: float = Field(..., description="Orientation angle in degrees (0-180)")
    morphology_type: str = Field(..., description="Morphological slick classification")

class ReleaseWindowResponse(BaseModel):
    earliest: str
    latest: str
    most_probable: str
    confidence_pct: int

class SlickDetectionResponse(BaseModel):
    data_provenance: str = Field(..., json_schema_extra={"example": "SIMULATED INVESTIGATION SCENARIO"})
    incident_id: str
    oil_probability: float
    lookalike_probability: float
    uncertainty: float
    classification: str
    class_probabilities: Dict[str, float]
    slick_geometry: SlickGeometryResponse
    estimated_release_window: ReleaseWindowResponse
    metrics: Dict[str, Any]

class DetectRequest(BaseModel):
    incident_id: str = "MARLIN-X-DEMO-001"
    satellite_source: str = "Sentinel-1B SAR"
    confidence_threshold: float = 0.45
