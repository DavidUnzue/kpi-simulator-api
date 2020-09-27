import json
from fastapi.testclient import TestClient
from pathlib import Path
from app.main import app

mocks_folder = Path(__file__).parent / "mocks"

client = TestClient(app)

with open(mocks_folder / "booking_distance_bins.json", "r") as file_contents:
    mock_booking_distance_bins = json.loads(file_contents.read())

with open(mocks_folder / "feature.json", "r") as file_contents:
    mock_feature = json.loads(file_contents.read())


def test_run_simulation():
    response = client.get("/kpis")
    response_body = response.json()
    assert response.status_code == 200

    assert response_body["booking_distance_bins"] == mock_booking_distance_bins

    dropoffs = json.loads(response_body["most_popular_dropoff_points"])
    assert "type" in dropoffs
    assert dropoffs["type"] == "FeatureCollection"
    assert "features" in dropoffs
    assert len(dropoffs["features"]) > 0
    assert set(dropoffs["features"][0]) == set(mock_feature)

    pickups = json.loads(response_body["most_popular_pickup_points"])
    assert "type" in pickups
    assert pickups["type"] == "FeatureCollection"
    assert "features" in pickups
    assert len(pickups["features"]) > 0
    assert set(pickups["features"][0]) == set(mock_feature)
