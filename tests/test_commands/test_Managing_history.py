# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock
import pytest
from app.History.Managing_History import history_manager
from app.calculator.calculations import Calculations

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

@pytest.fixture
def mock_get_history():
    '''Fixture to mock the get_history method'''
    mock_get = Mock()
    mock_get.return_value = []  # Mocking it to return an empty list for empty history
    Calculations.get_history = mock_get
    return mock_get

class TestManageHistory:
    def test_managing_history_empty(self):
        '''Test that get_latest() returns None when history is empty'''
        history = history_manager()  
        print(f"History before test: {history.get_latest()}")
        history.clear_history()
        assert history.get_latest() is None

    def test_managing_history_exception(self):
        '''Test that find_by_operation() raises an exception for invalid operations'''
        history = history_manager() 
        with pytest.raises(ValueError, match="No history available"):
            history.find_by_operation("invalid_op")