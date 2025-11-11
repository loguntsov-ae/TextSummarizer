"""
Tests for Worker and domain logic.
"""
import pytest
from unittest.mock import Mock, AsyncMock, patch
import sys
import os

# Add worker directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'worker'))


@pytest.mark.asyncio
async def test_handle_task_success(sample_text):
    """Test successful task handling."""
    from main import handle_task
    
    mock_message = {
        "task_id": "test-id-123",
        "text": sample_text
    }
    
    with patch('main.repo') as mock_repo, \
         patch('main.publish_result') as mock_publish:
        
        mock_repo.summarize = AsyncMock(return_value="Test summary")
        mock_publish.return_value = None
        
        await handle_task(mock_message)
        
        # Verify summarize was called
        mock_repo.summarize.assert_called_once_with(sample_text)
        
        # Verify result was published
        mock_publish.assert_called_once()
        call_args = mock_publish.call_args[0][0]
        assert call_args["task_id"] == "test-id-123"
        assert "summary" in call_args


@pytest.mark.asyncio
async def test_handle_task_error(sample_text):
    """Test task handling with error."""
    from main import handle_task
    
    mock_message = {
        "task_id": "test-id-456",
        "text": sample_text
    }
    
    with patch('main.repo') as mock_repo, \
         patch('main.publish_result') as mock_publish:
        
        # Simulate an error
        mock_repo.summarize = AsyncMock(side_effect=Exception("API Error"))
        mock_publish.return_value = None
        
        await handle_task(mock_message)
        
        # Should still publish result with error
        mock_publish.assert_called_once()
        call_args = mock_publish.call_args[0][0]
        assert "Error" in call_args["summary"]


def test_factory_returns_repository():
    """Test that factory returns a valid repository."""
    from domain.factory import get_repository
    from domain.interfaces import ModelRepository
    
    repo = get_repository()
    assert repo is not None
    assert isinstance(repo, ModelRepository)


def test_repository_has_summarize_method():
    """Test that repository has summarize method."""
    from domain.factory import get_repository
    
    repo = get_repository()
    assert hasattr(repo, 'summarize')
    assert callable(repo.summarize)
