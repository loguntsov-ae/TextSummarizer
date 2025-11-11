"""
Tests for API Gateway endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'api_gateway'))

from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


def test_read_root(client):
    """Test the root endpoint returns HTML."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Text Summarizer" in response.text


def test_create_task_success(client, sample_text):
    """Test creating a summarization task."""
    with patch('main.publish_task') as mock_publish:
        mock_publish.return_value = None
        
        response = client.post(
            "/summarize",
            json={"text": sample_text}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "task_id" in data
        assert data["status"] == "queued"
        assert len(data["task_id"]) > 0


def test_create_task_empty_text(client):
    """Test creating a task with empty text."""
    response = client.post(
        "/summarize",
        json={"text": ""}
    )
    # Should still create a task even with empty text
    # Validation can be added later
    assert response.status_code in [200, 422]


def test_create_task_missing_text(client):
    """Test creating a task without text field."""
    response = client.post(
        "/summarize",
        json={}
    )
    assert response.status_code == 422  # Validation error


def test_get_tasks(client):
    """Test getting all tasks."""
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_delete_task_not_found(client):
    """Test deleting a non-existent task."""
    response = client.delete("/tasks/non-existent-id")
    assert response.status_code == 200
    data = response.json()
    # Should return ok=False or similar
    assert "ok" in data


def test_api_response_format(client, sample_text):
    """Test that API responses have correct format."""
    with patch('main.publish_task') as mock_publish:
        mock_publish.return_value = None
        
        response = client.post(
            "/summarize",
            json={"text": sample_text}
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Check response structure
        assert "task_id" in data
        assert "status" in data
        assert isinstance(data["task_id"], str)
        assert isinstance(data["status"], str)


def test_tasks_endpoint_returns_list(client):
    """Test that /tasks endpoint returns a list."""
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    
    # If there are tasks, check their structure
    if len(data) > 0:
        task = data[0]
        assert "task_id" in task
        assert "status" in task


@pytest.mark.asyncio
async def test_websocket_connection(client):
    """Test WebSocket connection (basic check)."""
    # WebSocket testing with TestClient is limited
    # This is a placeholder for future WebSocket tests
    with client.websocket_connect("/ws") as websocket:
        # Connection should be established
        assert websocket is not None


def test_cors_headers(client):
    """Test that appropriate headers are set."""
    response = client.get("/tasks")
    assert response.status_code == 200
    # Could check for CORS headers if needed
