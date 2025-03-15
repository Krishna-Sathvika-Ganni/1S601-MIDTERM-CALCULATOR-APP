import pytest
from unittest.mock import Mock
from app.History.Managing_History import history_manager
from app.calculator.calculations import Calculations


@pytest.fixture
def mock_command_handler():
    '''Mock command handler'''
    mock_handler = Mock()
    mock_handler.register_command = Mock()
    mock_handler.execute_command = Mock()
    return mock_handler


@pytest.fixture
def mock_get_history():
    '''Fixture'''
    mock_get = Mock()
    mock_get.return_value = []  
    Calculations.get_history = mock_get
    return mock_get


class TestManageHistory:
    def test_managing_history_empty(self, mock_get_history):
        '''Test that get_latest() returns None when history is empty'''
        history = history_manager()  # No arguments needed
        print(f"History before test: {history.get_latest()}")
        history.clear_history()
        assert history.get_latest() is None

    def test_managing_history_exception(self, mock_get_history):
        '''Test that find_by_operation() raises an exception for invalid operations'''
        history = history_manager()  
        with pytest.raises(ValueError, match="No history available"):
            history.find_by_operation("invalid_op")

    def test_save_history(self, mock_get_history):
        '''Test that save_history saves history correctly'''
        history = history_manager() 
        mock_get_history.return_value = [Mock(x=1, y=2, operation=Mock(__name__='add'), perform=Mock(return_value=3))]
        history.save_history()
        pd_mock = Mock()
        pd_mock.to_csv.assert_called_once()
        assert pd_mock.to_csv.called

    def test_load_history(self):
        '''Test that load_history loads data correctly'''
        history = history_manager()
        history.load_history()  


    def test_clear_history(self):
        '''Test that clear_history clears the in-memory history'''
        history = history_manager()  
        history.clear_history()
        assert Calculations.get_history() == [] 

    def test_delete_history(self):
        '''Test that delete_history deletes the saved history file'''
        history = history_manager()  
        history.delete_history()
       
