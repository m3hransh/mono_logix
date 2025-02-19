import logging

import pytest

from monologix import log_monad  # Assuming your decorator is in 'your_module.py'


# Mock logger and handler for capturing log messages
class MemoryHandler(logging.Handler):
    messages: list[str]

    def __init__(self):
        super().__init__()
        self.messages = []

    def emit(self, record: logging.LogRecord):
        self.messages.append(self.format(record))

    def clear(self):
        self.messages.clear()


@pytest.fixture
def memory_handler():
    handler = MemoryHandler()
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)  # Ensure we capture all log levels
    yield handler
    logger.removeHandler(handler)


def test_log_monad_basic(memory_handler: MemoryHandler):
    @log_monad(error_message="An error occurred", logger=logging.getLogger(__name__))
    def sample_function() -> str:
        return "Success!"

    # Clear any existing messages
    memory_handler.clear()

    result = sample_function()

    assert result == "Success!"
    assert "Running sample_function" in memory_handler.messages[0]
    assert "sample_function returned: Success!" in memory_handler.messages[1]
    assert len(memory_handler.messages) == 2


def test_log_monad_with_error(memory_handler: MemoryHandler):
    @log_monad(error_message="An error occurred", logger=logging.getLogger(__name__))
    def sample_function() -> None:
        raise ValueError("Test error")

    # Clear any existing messages
    memory_handler.clear()

    with pytest.raises(ValueError):
        sample_function()

    assert "Running sample_function" in memory_handler.messages[0]
    assert "An error occurred: Test error" in memory_handler.messages[1]
    assert len(memory_handler.messages) == 2


def test_log_monad_with_warn_on_error(memory_handler: MemoryHandler):
    @log_monad(error_message="An error occurred", warn_on_error=True, logger=logging.getLogger(__name__))
    def sample_function() -> None:
        raise ValueError("Test error")

    # Clear any existing messages
    memory_handler.clear()

    with pytest.raises(ValueError):
        sample_function()

    assert "Running sample_function" in memory_handler.messages[0]
    assert "An error occurred: Test error" in memory_handler.messages[1]
    assert "sample_function failed" in memory_handler.messages[2]
    assert len(memory_handler.messages) == 3


def test_log_monad_with_info_on_error(memory_handler: MemoryHandler):
    @log_monad(error_message="An error occurred", info_on_error=True, logger=logging.getLogger(__name__))
    def sample_function() -> None:
        raise ValueError("Test error")

    # Clear any existing messages
    memory_handler.clear()

    with pytest.raises(ValueError):
        sample_function()

    assert "Running sample_function" in memory_handler.messages[0]
    assert "An error occurred: Test error" in memory_handler.messages[1]
    assert "sample_function failed" in memory_handler.messages[2]
    assert len(memory_handler.messages) == 3
