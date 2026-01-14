import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    """
    Тест: Успешное создание поста
    """
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "My New Post",
        "body": "This is the content of the post.",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 201, f"Expected status 201, got {response.status_code}"
    data = response.json()
    assert "id" in data, "Response should contain 'id'"
    assert data["title"] == payload["title"], "Title mismatch"
    assert data["body"] == payload["body"], "Body mismatch"
    assert data["userId"] == payload["userId"], "UserId mismatch"


def test_update_post():
    """
    Тест: Успешное изменение поста (PUT)
    """
    post_id = 1
    url = f"{BASE_URL}/posts/{post_id}"
    payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "Updated content of the post.",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}

    response = requests.put(url, json=payload, headers=headers)

    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    data = response.json()
    assert data["id"] == payload["id"], "ID mismatch after update"
    assert data["title"] == payload["title"], "Title not updated"
    assert data["body"] == payload["body"], "Body not updated"
    assert data["userId"] == payload["userId"], "UserId not updated"


def test_delete_post():
    """
    Тест: Успешное удаление поста
    """
    post_id = 1
    url = f"{BASE_URL}/posts/{post_id}"

    response = requests.delete(url)

    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.text.strip() in ("", "{}"), f"Expected empty or {{}}, got '{response.text}'"
