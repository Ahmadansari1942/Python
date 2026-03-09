import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_about_page():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200

def test_api_hello():
    client = app.test_client()
    response = client.get('/api/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'

def test_api_status():
    client = app.test_client()
    response = client.get('/api/status')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'running'

def test_404():
    client = app.test_client()
    response = client.get('/non-existent-page')
    assert response.status_code == 404
