import pytest
from Model import PersonModel

BASE_URL = '/person' 

def test_successful_person_list_return(client):
    response = client.get(f"{BASE_URL}/show")
    print("\nRetorno da consulta de todas pessoas:", response.json())

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_success_id_existent_return(client):
    response = client.get(f"{BASE_URL}/show/1") 
    print("\nRetorno da consulta de pessoa existente:", response.json())

    assert response.status_code == 200    
    assert isinstance(response.json(), dict)

    assert response.json()["id"] == 1

def test_error_id_non_existent_return(client):
    response = client.get(f"{BASE_URL}/show/3") 
    print("\nRetorno da consulta de pessoa nao existente:", response.json())
    
    assert response.status_code == 404    
    assert response.json()["detail"] == "Person not found" 