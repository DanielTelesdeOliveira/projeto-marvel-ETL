import pytest
from Model import Character

BASE_URL = '/characters' 

def test_successful_character_list_return(client):
    response = client.get(f"{BASE_URL}/show")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2
    assert isinstance(data, list)
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Tony Stark"
    assert "description" not in data[0]
    

def test_success_id_existent_return(client):
    response = client.get(f"{BASE_URL}/show/2") 
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 2
    assert data["name"] == "Peter Parker"
    assert "description" in data


def test_error_id_non_existent_return(client):
    response = client.get(f"{BASE_URL}/show/3") 
    assert response.status_code == 404    

    data = response.json()
    assert isinstance(data, dict)
    assert data["detail"] == "Character not found" 

def test_negative_id(client):
    response = client.get(f"{BASE_URL}/show/-1") 
    assert response.status_code == 400    

    data = response.json()
    assert isinstance(data, dict)
    assert data["detail"] == "Invalid character id" 
