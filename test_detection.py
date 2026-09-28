from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_run_detection():
    response = client.post("/api/v1/detect/run", json={"incident_id": "MARLIN-X-DEMO-001"})
    assert response.status_code == 200
    data = response.json()
    assert data["oil_probability"] == 0.88
    assert "data_provenance" in data
    assert "SIMULATED" in data["data_provenance"]
    assert data["metrics"]["validation_status"] == "MODEL NOT YET VALIDATED ON REAL SATELLITE DATASET"

def test_analyse_slick():
    response = client.post("/api/v1/slick/analyse", json={})
    assert response.status_code == 200
    data = response.json()
    assert data["area_sqkm"] == 14.85
    assert data["morphology_type"] == "Elongated Filamental Slick"
