import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "My New Post",
        "body": "This is the content of the post.",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_update_post():
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

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_delete_post():
    post_id = 1
    url = f"{BASE_URL}/posts/{post_id}"

    response = requests.delete(url)

    assert response.status_code == 200
    assert response.text == ""
