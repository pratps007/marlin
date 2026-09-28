from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_evidence_fusion_api():
    response = client.post("/api/v1/evidence/fuse?incident_id=MARLIN-X-DEMO-001")
    assert response.status_code == 200
    data = response.json()
    assert data["overall_investigation_priority"] == "HIGH"
    assert "evidence_for" in data
    assert "recommended_next_observation" in data

def test_report_generation_api():
    response = client.post("/api/v1/report/generate?incident_id=MARLIN-X-DEMO-001")
    assert response.status_code == 200
    assert "MARLIN-X MARINE POLLUTION FORENSIC REPORT" in response.text
    assert "SIMULATED INVESTIGATION SCENARIO" in response.text
