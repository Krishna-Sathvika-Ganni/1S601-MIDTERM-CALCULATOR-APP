# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock
import pytest
from app.plugins.savehistorycommand import SaveHistory

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def save_history_command(mock_command_handler):
    '''Fixture'''
    return SaveHistory(command_handler=mock_command_handler)

class test_save_history:
    '''Testing the save history command'''
    def test_save_history(self, save_history_command, capsys):
        '''Testing'''
        save_history_command.execute()
        captured = capsys.readouterr()
        assert "History saved successfully" in captured.out

# End of program
