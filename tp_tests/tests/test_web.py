import pytest
from app.web import create_app
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
def test_message_normal(client):
    response = client.post(
        "/moderate",
        json={"message": "bonjour"})
    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}
def test_message_spam(client):
    response = client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}  )
    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}
def test_message_absent(client):
    response = client.post("/moderate", json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}
def test_message_type_invalide(client):
    response = client.post(
        "/moderate",
        json={"message": 42}
    )
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}
def test_message_vide(client):
    response = client.post(
        "/moderate",
        json={"message": "   "}
    )
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}
def test_json_liste(client):
    response = client.post("/moderate", json=["bonjour"])
    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}