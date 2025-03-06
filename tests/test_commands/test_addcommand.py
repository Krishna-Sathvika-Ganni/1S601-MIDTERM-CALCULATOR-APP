# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock, patch
import pytest
from app.plugins.addcommand import Add


@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def add_command(mock_command_handler):
    '''Fixture'''
    return Add(command_handler=mock_command_handler)

class TestAddCommand:
    '''Test the Add command.'''
    def test_add(self,add_command, capsys):
        '''Testing the add command'''
        add_command.execute('2', '3')
        captured=capsys.readouterr()
        assert "2 + 3 = 5" in captured.out

    def test_add_one_argument(self,add_command, capsys):
        '''Testing when only one argument is given'''
        add_command.execute('2')
        captured=capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_add_invalid_args(self, add_command,capsys):
        '''Testing for invalid arguments'''
        add_command.execute('x','2')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_add_error(self, add_command, capsys):
        '''Testing for invalid arguments'''
        with patch('app.plugins.addcommand.Calculator.add', side_effect=ValueError("Error")):
            add_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out

# End of program
