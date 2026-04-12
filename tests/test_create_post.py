import requests


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {"title": "my test post", "body": "hello from autotest", "userId": 1}

    response = requests.post(url, json=payload)

    # Проверяем статус код
    assert response.status_code == 201

    response_json = response.json()

    # Проверяем, что данные в ответе такие же
    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]
    assert response_json["userId"] == payload["userId"]
    assert "id" in response_json
    assert isinstance(response_json["id"], int)