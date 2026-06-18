from fastapi.testclient import TestClient
from starter_code import app

client = TestClient(app)

def test_create_and_get_item():
    resp = client.post('/items/', json={'name': 'Widget', 'description': 'A widget', 'price': 3.5})
    assert resp.status_code == 201
    data = resp.json()
    assert data['id'] == 1

    resp2 = client.get(f"/items/{data['id']}")
    assert resp2.status_code == 200
    assert resp2.json()['name'] == 'Widget'
