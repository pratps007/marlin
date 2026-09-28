from fastapi import APIRouter
from app.services.evidence_service import evidence_engine

router = APIRouter()

@router.post("/fuse")
def fuse_evidence(incident_id: str = "MARLIN-X-DEMO-001"):
    """Fuses 8 evidence channels and returns explainable assessment & next observation recommendation."""
    return evidence_engine.fuse_evidence_for_incident(incident_id)
