import requests
def test_create_post_without_required_fields():
    url = "https://jsonplaceholder.typicode.com/posts"

    # ❌ отправляем некорректные данные
    payload = {}

    response = requests.post(url, json=payload)

    # ❗ В реальном API тут был бы 400
    # но так как это mock, он всё равно вернёт 201
    assert response.status_code == 201
