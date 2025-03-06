# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock
import pytest
from app.plugins.clearhistorycommand import ClearHistory

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def clear_history_command(mock_command_handler):
    '''Fixture'''
    return ClearHistory(command_handler=mock_command_handler)

class test_clear_history:
    '''Testing the clear history command'''
    def test_clear(self, clear_history_command, capsys):
        '''Testing'''
        clear_history_command.execute()
        captured = capsys.readouterr()
        assert "History cleared successfully" in captured.out

# End of program
