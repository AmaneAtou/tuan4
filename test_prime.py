import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_with_prime():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

def test_check_prime_with_non_prime():
    response = client.get("/check_prime/8")
    assert response.status_code == 200
    assert response.json() == {"number": 8, "is_prime": False}

def test_check_prime_with_1():
    response = client.get("/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}

def test_check_prime_with_negative():
    response = client.get("/check_prime/-5")
    assert response.status_code == 200
    assert response.json() == {"number": -5, "is_prime": False}

def test_check_prime_with_0():
    response = client.get("/check_prime/0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_with_large_prime():
    response = client.get("/check_prime/7919")
    assert response.status_code == 200
    assert response.json() == {"number": 7919, "is_prime": True}

def test_check_prime_with_large_non_prime():
    response = client.get("/check_prime/10000")
    assert response.status_code == 200
    assert response.json() == {"number": 10000, "is_prime": False}

def test_check_prime_with_even():
    response = client.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_check_prime_with_large_even():
    response = client.get("/check_prime/10002")
    assert response.status_code == 200
    assert response.json() == {"number": 10002, "is_prime": False}
