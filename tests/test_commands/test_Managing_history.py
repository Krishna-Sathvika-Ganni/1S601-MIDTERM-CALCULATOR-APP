# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock
import pytest
from app.History.Managing_History import history_manager

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.register_command=Mock()
    mock_handler.execute_command=Mock()
    return mock_handler

@pytest.fixture
def manage_history(mock_command_handler):
    '''Fixture'''
    return history_manager(command_handler=mock_command_handler)

class ManageHistory:
    def test_managing_history_empty():
        history = history_manager()
        assert history.get_latest() is None  

    def test_managing_history_exception():
        history = history_manager()
        try:
            history.find_by_operation("invalid_op")  
        except ValueError as e:
            assert str(e) == "Invalid operation"