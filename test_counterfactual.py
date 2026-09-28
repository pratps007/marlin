from fastapi.testclient import TestClient
from app.main import app
from app.services.counterfactual_service import counterfactual_engine

client = TestClient(app)

def test_counterfactual_service():
    res = counterfactual_engine.compute_counterfactual_compatibility(
        mmsi="413291000",
        vessel_release_pos=(12.80, 74.16),
        vessel_release_time="2026-09-28 03:30 UTC"
    )
    assert res["physical_compatibility_score_pct"] == 89.0
    assert res["metrics"]["spatial_iou_overlap_pct"] == 86.4
    assert "NOT legal proof" in res["scientific_label"]

def test_counterfactual_api():
    response = client.post("/api/v1/counterfactual/simulate", json={
        "mmsi": "413291000",
        "vessel_release_pos": [12.80, 74.16]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["physical_compatibility_score_pct"] == 89.0
    assert data["mmsi"] == "413291000"
