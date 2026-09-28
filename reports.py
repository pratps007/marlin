from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.services.report_service import report_engine

router = APIRouter()

@router.post("/generate", response_class=HTMLResponse)
def generate_report(incident_id: str = "MARLIN-X-DEMO-001"):
    """Generates printable HTML investigation report with evidence provenance."""
    return report_engine.generate_html_report(incident_id)
