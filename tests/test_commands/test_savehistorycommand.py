# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock, patch
import pytest
from app.plugins.savehistorycommand import SaveHistory

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler = Mock()
    mock_handler.Register_Command = Mock()
    mock_handler.Execute_Command = Mock()
    return mock_handler

@pytest.fixture
def save_history_command(mock_command_handler):
    '''Fixture'''
    return SaveHistory(command_handler=mock_command_handler)

class TestSaveHistory:
    '''Testing the save history command'''

    def test_save_history(self, save_history_command, capsys):
        '''Test if history saves successfully'''
        save_history_command.execute()
        captured = capsys.readouterr()
        assert "There is no history to save" in captured.out

    def test_save_history_called(self, save_history_command):
        '''Ensure save_history is called'''
        with patch.object(save_history_command.history_facade, 'save_history') as mock_save:
            save_history_command.execute()
            mock_save.assert_called_once()

    def test_save_history_exception(self, save_history_command, capsys):
        '''Test handling of save history failure'''
        with patch.object(save_history_command.history_facade, 'save_history', side_effect=Exception("Save failed")):
            save_history_command.execute()
            captured = capsys.readouterr()
            assert "Save failed" in captured.out

    def test_save_history_no_command_handler(self):
        '''Test behavior when command handler is None'''
        command = SaveHistory(command_handler=None)
        assert command.command_handler is None

    def test_save_empty_history(self, save_history_command, capsys):
        '''Test saving when history is empty'''
        with patch.object(save_history_command.history_facade, 'save_history', return_value="No history to save"):
            save_history_command.execute()
            captured = capsys.readouterr()
            assert "No history to save" in captured.out

    def test_save_large_history(self, save_history_command, capsys):
        '''Test saving when history is large'''
        large_history = [f"Entry {i}".format(i) for i in range(10000)]
        with patch.object(save_history_command.history_facade, 'save_history', return_value="Large history saved"):
            save_history_command.execute()
            captured = capsys.readouterr()
            assert "Large history saved" in captured.out
