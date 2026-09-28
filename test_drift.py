from fastapi.testclient import TestClient
from app.main import app
from app.services.drift_service import drift_engine

client = TestClient(app)

def test_backward_hindcast_service():
    res = drift_engine.simulate_backward_hindcast(
        slick_centroid=(12.85, 74.22),
        wind_speed_knots=12.5,
        wind_dir_deg=240.0,
        current_speed_mps=0.45,
        current_dir_deg=115.0,
        hours_back=6.0
    )
    assert res["hours_hindcast"] == 6.0
    assert "probabilistic_corridors" in res
    assert "contour_50_pct" in res["probabilistic_corridors"]

def test_backward_drift_api():
    response = client.post("/api/v1/drift/backward", json={
        "slick_centroid": [12.85, 74.22],
        "hours_back": 6.0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["simulation_type"] == "Probabilistic Reversible Lagrangian Hindcast"
    assert len(data["particles"]) > 0

def test_forward_drift_api():
    response = client.post("/api/v1/drift/forward", json={
        "origin_point": [12.80, 74.16]
    })
    assert response.status_code == 200
    data = response.json()
    assert "+24h" in data["timesteps"]
