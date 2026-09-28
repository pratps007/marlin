from pydantic import BaseModel, Field
from typing import Dict, Any

class SystemStatusResponse(BaseModel):
    status: str = Field(..., json_schema_extra={"example": "healthy"})
    project: str = Field(..., json_schema_extra={"example": "MARLIN-X"})
    version: str = Field(..., json_schema_extra={"example": "1.0.0-SIH2026"})
    demo_mode: bool = Field(..., json_schema_extra={"example": True})
    active_incidents: int = Field(..., json_schema_extra={"example": 1})
    services: Dict[str, str] = Field(
        ...,
        json_schema_extra={
            "example": {
                "sar_ml_engine": "ONLINE",
                "lagrangian_drift": "ONLINE",
                "ais_forensics": "ONLINE",
                "counterfactual_sim": "ONLINE"
            }
        }
    )

class HealthCheckResponse(BaseModel):
    status: str = "ok"
    timestamp: str
