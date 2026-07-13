import pytest
from Model import PersonModel

BASE_URL = '/person' 

def test_successful_person_list_return(client):
    response = client.get(f"{BASE_URL}/show")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Stan Lee"
    
def test_success_id_existent_return(client):
    response = client.get(f"{BASE_URL}/show/2") 
    assert response.status_code == 200    
    assert response.headers["content-type"] == "application/json"

    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 2
    assert data["name"] == "Jack Kirby"

def test_error_id_non_existent_return(client):
    response = client.get(f"{BASE_URL}/show/3") 
    assert response.status_code == 404    

    data = response.json()
    assert isinstance(data, dict)
    assert data["detail"] == "Person not found" 

def test_error_negative_id(client):
    response = client.get(f"{BASE_URL}/show/-1") 
    assert response.status_code == 400    

    data = response.json()
    assert isinstance(data, dict)
    assert data["detail"] == "Invalid person id" 
