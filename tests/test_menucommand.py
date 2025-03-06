# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock, patch
import pytest
from app.plugins.menucommand import Menu


@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def menu_command(mock_command_handler):
    '''Fixture for Menu Command'''
    # Correct the MockCommandHandler to return the list of commands
    mock_command_handler.Get_Registered_Commands = Mock(return_value=["Add","Menu"])
    return Menu(command_handler=mock_command_handler)

# Testing menu command

class TestMenuCommand:
    '''Test the Menu command'''
    def test_menu_command(self, menu_command, capsys):
        '''Test that the Menu command displays the list of available commands.'''
        menu_command.execute()
        captured = capsys.readouterr()
        assert "Commands Available:" in captured.out, "MenuCommand should display the available commands"
        assert "Add" in captured.out
        assert "Menu" in captured.out