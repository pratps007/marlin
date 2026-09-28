from fastapi import APIRouter
from app.schemas.slick import DetectRequest, SlickDetectionResponse, SlickGeometryResponse, ReleaseWindowResponse

router = APIRouter()

@router.post("/run", response_model=SlickDetectionResponse)
def run_detection(req: DetectRequest):
    return SlickDetectionResponse(
        data_provenance="SIMULATED INVESTIGATION SCENARIO (DEMO MODE)",
        incident_id=req.incident_id,
        oil_probability=0.88,
        lookalike_probability=0.08,
        uncertainty=0.04,
        classification="Probable Oil Slick (Simulated Scenario)",
        class_probabilities={
            "Probable Oil Slick": 0.88,
            "Environmental Look-alike (Low Wind)": 0.05,
            "Environmental Look-alike (Biogenic Film)": 0.03,
            "Uncertain / Human Review Required": 0.04
        },
        slick_geometry=SlickGeometryResponse(
            area_sqkm=14.85,
            perimeter_km=26.4,
            centroid=(12.85, 74.22),
            length_km=8.2,
            width_km=2.1,
            orientation_deg=135.0,
            morphology_type="Elongated Filamental Slick"
        ),
        estimated_release_window=ReleaseWindowResponse(
            earliest="2026-09-28 01:15 UTC",
            latest="2026-09-28 05:45 UTC",
            most_probable="2026-09-28 03:30 UTC",
            confidence_pct=84
        ),
        metrics={
            "validation_status": "MODEL NOT YET VALIDATED ON REAL SATELLITE DATASET",
            "IoU": "N/A",
            "Dice": "N/A",
            "Precision": "N/A",
            "Recall": "N/A"
        }
    )
