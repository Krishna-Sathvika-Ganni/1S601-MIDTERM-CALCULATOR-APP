# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock
import pytest
from app.plugins.deletehistorycommand import DeleteHistory

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def delete_history_command(mock_command_handler):
    '''Fixture'''
    return DeleteHistory(command_handler=mock_command_handler)

class test_delete_history:
    '''Testing the delete history command'''
    def test_delete(self, delete_history_command, capsys):
        '''Testing'''
        delete_history_command.execute()
        captured = capsys.readouterr()
        assert "History deleted successfully" in captured.out

# End of program
