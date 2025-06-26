from app import app

def test_home():
    client = app.test_client()
    response = client.get('/hello1')
    assert response.status_code == 200
    assert b"Hello from Flask" in response.data
