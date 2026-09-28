from fastapi import APIRouter
from app.api.endpoints import system, detection, slick, ais, drift, counterfactual, evidence, reports

api_router = APIRouter()
api_router.include_router(system.router, prefix="/system", tags=["System"])
api_router.include_router(detection.router, prefix="/detect", tags=["Detection"])
api_router.include_router(slick.router, prefix="/slick", tags=["Slick Analytics"])
api_router.include_router(ais.router, prefix="/ais", tags=["AIS Forensics"])
api_router.include_router(ais.router, prefix="/vessels", tags=["Vessel Candidates"])
api_router.include_router(drift.router, prefix="/drift", tags=["Lagrangian Drift Engine"])
api_router.include_router(counterfactual.router, prefix="/counterfactual", tags=["Counterfactual Simulation Engine"])
api_router.include_router(evidence.router, prefix="/evidence", tags=["Multi-Evidence Fusion Engine"])
api_router.include_router(reports.router, prefix="/report", tags=["Report Generation Engine"])
