"""
Test configuration and shared fixtures.
"""
import pytest
import asyncio
from typing import Generator


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def sample_text() -> str:
    """Sample text for testing summarization."""
    return (
        "Artificial intelligence is transforming the world. "
        "Machine learning enables computers to learn from data without being explicitly programmed. "
        "Deep learning uses neural networks with multiple layers to process information."
    )


@pytest.fixture
def short_text() -> str:
    """Short text for testing."""
    return "This is a short test text."


@pytest.fixture
def long_text() -> str:
    """Long text for testing."""
    return (
        "The Apollo 11 mission was a historic spaceflight that landed the first humans on the Moon. "
        "Commander Neil Armstrong and lunar module pilot Buzz Aldrin landed the Apollo Lunar Module Eagle "
        "on July 20, 1969. Armstrong became the first person to step onto the lunar surface six hours and "
        "39 minutes later. Aldrin joined him 19 minutes later. They spent about two and a quarter hours "
        "together outside the spacecraft, and collected 47.5 pounds of lunar material to bring back to Earth. "
        "Command module pilot Michael Collins flew the command module Columbia alone in lunar orbit while they "
        "were on the Moon's surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface at "
        "a site they had named Tranquility Base before lifting off to rejoin Columbia in lunar orbit."
    )
