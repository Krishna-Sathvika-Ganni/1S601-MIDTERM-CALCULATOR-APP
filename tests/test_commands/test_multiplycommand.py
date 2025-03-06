'''This is test_multiplycommand file'''
from unittest.mock import Mock, patch
import pytest
from app.plugins.addcommand import Add
from app.plugins.subtractcommand import Subtract
from app.plugins.multiplycommand import Multiply
from app.plugins.menucommand import Menu

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def multiply_command(mock_command_handler):
    '''Fixture'''
    return Multiply(command_handler=mock_command_handler)

# Testing the Multiply command:
class TestMultiplyCommand:
    def test_multiply(self,multiply_command,capsys):
        '''Testing multiply command'''
        multiply_command.execute('4','2')
        captured=capsys.readouterr()
        assert "4 x 2 = 8" in captured.out

    def test_multiply_one_arg(self,multiply_command,capsys):
        '''Testing one argument'''
        multiply_command.execute('4')
        captured=capsys.readouterr()
        assert "Only two arguments must be given" in captured.out


    def test_multiply_invalid_arg(self,multiply_command,capsys):
        '''Testing invalid argument'''
        multiply_command.execute('x','3')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_multiply_error(self, multiply_command, capsys):
        '''Testing for invalid arguments'''
        with patch('app.plugins.multiplycommand.Calculator.multiply', side_effect=ValueError("Error")):
            multiply_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out