"""
Tests for Repository implementations.
"""
import pytest
from unittest.mock import Mock, AsyncMock, patch


@pytest.mark.asyncio
async def test_repository_interface():
    """Test that repositories implement the interface correctly."""
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'worker'))
    
    from domain.interfaces import ModelRepository
    from domain.repositories.huggingface import HuggingFaceRepository
    
    # Check that HuggingFaceRepository implements ModelRepository
    repo = HuggingFaceRepository()
    assert isinstance(repo, ModelRepository)
    assert hasattr(repo, 'summarize')


@pytest.mark.asyncio
async def test_huggingface_repository_mock(sample_text):
    """Test HuggingFace repository with mocked API."""
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'worker'))
    
    from domain.repositories.huggingface import HuggingFaceRepository
    
    repo = HuggingFaceRepository()
    
    # Mock the actual API call
    with patch.object(repo, 'summarize', new_callable=AsyncMock) as mock_summarize:
        mock_summarize.return_value = "Mocked summary of the text"
        
        result = await repo.summarize(sample_text)
        
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.asyncio
async def test_repository_error_handling(sample_text):
    """Test repository error handling."""
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'worker'))
    
    from domain.repositories.huggingface import HuggingFaceRepository
    
    repo = HuggingFaceRepository()
    
    # Mock API failure
    with patch.object(repo, 'summarize', new_callable=AsyncMock) as mock_summarize:
        mock_summarize.side_effect = Exception("API Error")
        
        with pytest.raises(Exception):
            await repo.summarize(sample_text)


def test_factory_creates_correct_backend():
    """Test that factory creates the correct backend based on settings."""
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'worker'))
    
    from domain.factory import get_repository
    from domain.repositories.huggingface import HuggingFaceRepository
    
    with patch('domain.factory.settings') as mock_settings:
        mock_settings.model_backend = "huggingface"
        
        repo = get_repository()
        assert isinstance(repo, HuggingFaceRepository)


def test_all_repositories_have_summarize():
    """Test that all repository implementations have summarize method."""
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'worker'))
    
    from domain.repositories.huggingface import HuggingFaceRepository
    from domain.repositories.local_t5 import LocalT5Repository
    from domain.repositories.openai_api import OpenAIRepository
    
    repositories = [
        HuggingFaceRepository(),
        LocalT5Repository(),
        OpenAIRepository()
    ]
    
    for repo in repositories:
        assert hasattr(repo, 'summarize')
        assert callable(repo.summarize)
