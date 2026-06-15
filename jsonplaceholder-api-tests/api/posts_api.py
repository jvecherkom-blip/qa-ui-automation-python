import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def create_post(payload):
    response = requests.post(
        url=f"{BASE_URL}/posts",
        json=payload
    )
    return response

def get_post(post_id):
    return requests.get(
        url=f"{BASE_URL}/posts/{post_id}"
    )

def test_create_post_empty_body():
    response = requests.post(BASE_URL, json={})
    assert response.status_code in [400, 422]

def test_create_post_invalid_userid_type():
    payload = {
        "title": "Test",
        "body": "Test body",
        "userId": "string_instead_of_int"
    }

    response = requests.post(BASE_URL, json=payload)
    assert response.status_code in [400, 422]

def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/999999")
    assert response.status_code == 404

def test_create_post_long_title():
    payload = {
        "title": "A" * 1000,
        "body": "Test",
        "userId": 1
    }

    response = requests.post(BASE_URL, json=payload)
    assert response.status_code in [201, 400]
