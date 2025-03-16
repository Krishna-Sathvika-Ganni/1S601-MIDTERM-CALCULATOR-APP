# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock, patch
import pytest
from app.plugins.clearhistorycommand import ClearHistory

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler = Mock()
    mock_handler.Register_Command = Mock()
    mock_handler.Execute_Command = Mock()
    return mock_handler

@pytest.fixture
def clear_history_command(mock_command_handler):
    '''Fixture'''
    return ClearHistory(command_handler=mock_command_handler)

class TestClearHistory:
    '''Testing the clear history command'''

    def test_clear(self, clear_history_command, capsys):
        '''Test when history is cleared successfully'''
        clear_history_command.execute()
        captured = capsys.readouterr()
        assert "History cleared successfully" in captured.out

    def test_clear_history_success(self, clear_history_command, capsys):
        '''Test when history is successfully cleared'''
        with patch.object(clear_history_command.history_facade, 'clear_history', return_value="History cleared"):
            clear_history_command.execute()
            captured = capsys.readouterr()
            assert "History cleared" in captured.out

    def test_clear_no_history(self, clear_history_command, capsys):
        '''Test when there is no history to clear'''
        with patch.object(clear_history_command.history_facade, 'clear_history', return_value="No history to clear"):
            clear_history_command.execute()
            captured = capsys.readouterr()
            assert "No history to clear" in captured.out

    def test_clear_history_exception(self, clear_history_command, capsys):
        '''Test handling of failure during clearing history'''
        with patch.object(clear_history_command.history_facade, 'clear_history', side_effect=Exception("Failed to clear history")):
            clear_history_command.execute()
            captured = capsys.readouterr()
            assert "Failed to clear history" in captured.out

    def test_clear_history_called(self, clear_history_command):
        '''Ensure clear_history is called'''
        with patch.object(clear_history_command.history_facade, 'clear_history') as mock_clear:
            clear_history_command.execute()
            mock_clear.assert_called_once()

    def test_clear_history_no_command_handler(self):
        '''Test behavior when command handler is None'''
        command = ClearHistory(command_handler=None)
        with patch.object(command.history_facade, 'clear_history', return_value="History cleared"):
            command.execute()
