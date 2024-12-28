import pytest
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

@pytest.mark.parametrize("number, expected", [
    (2, True),    
    (3, True),    
    (4, False),   
    (5, True),   
    (9, False),  
    (11, True),   
    (1, False),   
    (0, False),   
    (13, True),   
    (25, False), 
])
def test_check_prime(number, expected):
    response = client.get(f"/check_prime/{number}")
    assert response.status_code == 200
    assert response.json()["is_prime"] == expected

