import requests
import pytest

api_url = 'https://petstore.swagger.io/v2'

def test_create_pet_positive():
    payload = {
        "id": 12345,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post(f'{api_url}/pet', json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
    assert response.json()['id'] == 12345

def test_create_pet_negative():
    payload = {
        "id": 9223372036854775808,
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "stock"
    }
    response = requests.post(f'{api_url}/pet', json=payload)
    print(f"Response: {response.text}")  # Print the response content for debugging
    assert response.status_code == 500, f"Unexpected status code: {response.status_code}, Response: {response.text}"

def test_get_pet_positive():
    pet_id = 12345
    response = requests.get(f'{api_url}/pet/{pet_id}')
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
    assert response.json()['id'] == pet_id

def test_get_pet_negative():
    pet_id = 999999  # Non-existent pet ID
    response = requests.get(f'{api_url}/pet/{pet_id}')
    assert response.status_code == 404, f"Unexpected status code: {response.status_code}, Response: {response.text}"

def test_update_pet_positive():
    payload = {
        "id": 12345,
        "name": "UpdatedTestPet",
        "photoUrls": [],
        "tags": [],
        "status": "sold"
    }
    response = requests.put(f'{api_url}/pet', json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
    assert response.json()['name'] == "UpdatedTestPet"

def test_update_pet_negative():
    payload = {
        "id": 1,
        "category": [
            "id",
            "name"
        ],
        "name": "cat",
        "photoUrls": [],
        "tags": [],
        "status": "sold"
    }
    response = requests.put(f'{api_url}/pet', json=payload)
    print(f"Response: {response.text}")  # Print the response content for debugging
    assert response.status_code == 500, f"Unexpected status code: {response.status_code}, Response: {response.text}"

def test_delete_pet_positive():
    pet_id = 12345
    response = requests.delete(f'{api_url}/pet/{pet_id}')
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"

def test_delete_pet_negative():
    pet_id = 999999  # Non-existent pet ID
    response = requests.delete(f'{api_url}/pet/{pet_id}')
    assert response.status_code == 404, f"Unexpected status code: {response.status_code}, Response: {response.text}"
