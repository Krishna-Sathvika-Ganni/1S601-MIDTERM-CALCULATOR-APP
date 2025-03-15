from unittest.mock import Mock
import pytest
from app.History.Facade_History import HistoryFacade
from app.History.Managing_History import history_manager

@pytest.fixture
def mock_history_manager():
    '''Mock the history_manager'''
    mock_manager = Mock(spec=history_manager)
    return mock_manager

@pytest.fixture
def history_facade(mock_history_manager):
    '''Fixture'''
    return HistoryFacade()

class TestFacadeHistory:
    def test_save_history(self, history_facade, mock_history_manager):
        '''Testing that save_history'''
        history_facade.save_history()
        mock_history_manager.save_history.assert_called_once()

    def test_load_history(self, history_facade, mock_history_manager):
        '''Testing that load_history '''
        history_facade.load_history()
        mock_history_manager.load_history.assert_called_once()

    def test_clear_history(self, history_facade, mock_history_manager):
        '''Testing that clear_history'''
        history_facade.clear_history()
        mock_history_manager.clear_history.assert_called_once()

    def test_delete_history(self, history_facade, mock_history_manager):
        '''Testing that delete_history '''
        history_facade.delete_history()
        mock_history_manager.delete_history.assert_called_once()
