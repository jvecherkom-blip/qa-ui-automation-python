from api.posts_api import create_post


def test_create_post_with_parametrized_fixture(post_payload):
    response = create_post(post_payload)
    response_json = response.json()

    assert response.status_code == 201
    assert response_json["title"] == post_payload["title"]
    assert response_json["body"] == post_payload["body"]
    assert response_json["userId"] == post_payload["userId"]
