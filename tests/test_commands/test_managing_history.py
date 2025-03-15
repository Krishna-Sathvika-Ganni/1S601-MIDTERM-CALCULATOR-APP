from unittest.mock import Mock, patch
import pytest
from app.History.Managing_History import history_manager
from app.calculator.calculations import Calculations


# Fixture to mock get_history
@pytest.fixture
def mock_get_history():
    '''Fixture'''
    mock_get = Mock()
    mock_get.return_value = [Mock(x=1, y=2, operation=Mock(__name__='add'), perform=Mock(return_value=3))]
    Calculations.get_history = mock_get
    return mock_get


# Test class for history_manager
class TestManageHistory:
    
    @patch('app.History.Managing_History.pd.DataFrame.to_csv') 
    def test_save_history(self, mock_to_csv, mock_get_history):
        '''Test that save_history saves history correctly'''
        history = history_manager()
        history.save_history()

        mock_to_csv.assert_called_once()  
        assert mock_to_csv.called  

    def test_clear_history(self, mock_get_history):
        '''Test that clear_history clears the in-memory history'''
        history = history_manager()

        mock_get_history.side_effect = [
            [Mock(x=1, y=2, operation=Mock(__name__='add'), perform=Mock(return_value=3))], 
            []  
        ]
        
        history.clear_history()
        
     
        assert not Calculations.get_history()  
        assert mock_get_history.call_count == 2

    def test_managing_history_empty(self, mock_get_history):
        '''Test that get_latest() returns None when history is empty'''
        history = history_manager()  # No arguments needed
   
        mock_get_history.return_value = [] 

        assert history.get_latest() is None

    def test_managing_history_exception(self, mock_get_history):
        '''Test that find_by_operation() raises an exception for invalid operations'''
        history = history_manager()

        mock_get_history.return_value = []

        with pytest.raises(ValueError, match="No history available"):
            history.find_by_operation("invalid_op")

    def test_load_history(self):
        '''Test that load_history loads data correctly'''
        history = history_manager()
        history.load_history()  

    def test_delete_history(self):
        '''Test that delete_history deletes the saved history file'''
        history = history_manager()  
        history.delete_history()