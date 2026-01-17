import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Replace with a valid activity name from your app
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "testuser@example.com"
    # Sign up
    signup_url = f"/activities/{activity_name}/signup?email={email}"
    response = client.post(signup_url)
    assert response.status_code == 200
    # Unregister
    unregister_url = f"/activities/{activity_name}/unregister?email={email}"
    response = client.post(unregister_url)
    assert response.status_code == 200
