# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock
import pytest
from app.plugins.loadhistorycommand import LoadHistory

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def load_history_command(mock_command_handler):
    '''Fixture'''
    return LoadHistory(command_handler=mock_command_handler)

class test_load_history:
    '''Testing the Load history command'''
    def test_load_history(self, load_history_command, capsys):
        '''Testing'''
        load_history_command.execute()
        captured = capsys.readouterr()
        assert "History loaded successfully" in captured.out

# End of program
