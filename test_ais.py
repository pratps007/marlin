from fastapi.testclient import TestClient
from app.main import app
from app.services.ais_service import haversine_distance_km, ais_engine

client = TestClient(app)

def test_haversine_distance():
    # Mangalore to Mumbai approximate distance check (~700 km)
    dist = haversine_distance_km(12.85, 74.22, 18.96, 72.82)
    assert 650.0 < dist < 750.0

def test_get_vessels():
    response = client.get("/api/v1/ais/vessels")
    assert response.status_code == 200
    vessels = response.json()
    assert len(vessels) == 4
    assert any(v["mmsi"] == "413291000" for v in vessels)

def test_vessel_track():
    response = client.get("/api/v1/ais/track/413291000")
    assert response.status_code == 200
    data = response.json()
    assert data["mmsi"] == "413291000"
    assert data["name"] == "OCEAN HYDRA"
    assert len(data["track"]) > 0

def test_ais_anomaly_audit():
    response = client.post("/api/v1/ais/anomaly?mmsi=413291000")
    assert response.status_code == 200
    data = response.json()
    assert data["reliability"] == "Suspicious"
    assert data["has_blackout"] is True
