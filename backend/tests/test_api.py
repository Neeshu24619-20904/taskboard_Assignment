"""
Backend API tests.
Uses SQLite in-memory so no external database is required.
"""
import os

os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from app.main import app


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _client():
    return TestClient(app)


# ---------------------------------------------------------------------------
# Health / root
# ---------------------------------------------------------------------------
def test_health():
    with _client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "UP"}


def test_root():
    with _client() as client:
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["service"] == "TaskBoard API"
        assert data["version"] == "1.0.0"


def test_ready():
    with _client() as client:
        response = client.get("/ready")
        assert response.status_code == 200
        assert response.json() == {"status": "READY"}


# ---------------------------------------------------------------------------
# Tasks — CRUD
# ---------------------------------------------------------------------------
def test_create_task():
    with _client() as client:
        payload = {
            "title": "Deploy application",
            "description": "Push to production cluster",
            "priority": "HIGH",
            "assignee": "Student",
        }
        response = client.post("/api/tasks", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Deploy application"
        assert data["priority"] == "HIGH"
        assert data["status"] == "TODO"
        assert "id" in data
        assert "created_at" in data


def test_list_tasks():
    with _client() as client:
        # Seed at least one task
        client.post("/api/tasks", json={"title": "List test task", "priority": "LOW"})
        response = client.get("/api/tasks")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) >= 1


def test_get_task():
    with _client() as client:
        created = client.post(
            "/api/tasks",
            json={"title": "Get me", "priority": "MEDIUM"},
        ).json()
        task_id = created["id"]

        response = client.get(f"/api/tasks/{task_id}")
        assert response.status_code == 200
        assert response.json()["id"] == task_id
        assert response.json()["title"] == "Get me"


def test_update_task_status():
    with _client() as client:
        task_id = client.post(
            "/api/tasks",
            json={"title": "Update me", "priority": "LOW"},
        ).json()["id"]

        response = client.put(
            f"/api/tasks/{task_id}",
            json={"status": "IN_PROGRESS"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == "IN_PROGRESS"


def test_delete_task():
    with _client() as client:
        task_id = client.post(
            "/api/tasks",
            json={"title": "Delete me", "priority": "HIGH"},
        ).json()["id"]

        del_response = client.delete(f"/api/tasks/{task_id}")
        assert del_response.status_code == 204

        get_response = client.get(f"/api/tasks/{task_id}")
        assert get_response.status_code == 404


def test_get_task_not_found():
    with _client() as client:
        response = client.get("/api/tasks/999999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Task not found"


def test_create_task_missing_title_fails():
    with _client() as client:
        response = client.post(
            "/api/tasks",
            json={"priority": "HIGH"},
        )
        assert response.status_code == 422


def test_stats():
    with _client() as client:
        response = client.get("/api/tasks/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total" in data
        assert "todo" in data
        assert "inProgress" in data
        assert "done" in data
        assert data["total"] >= 0
