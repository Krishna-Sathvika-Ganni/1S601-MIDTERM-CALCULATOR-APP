# pylint: disable=missing-class-docstring
from unittest.mock import Mock, patch
import pytest
from app.plugins.subtractcommand import Subtract

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def subtract_command(mock_command_handler):
    '''Fixture'''
    return Subtract(command_handler=mock_command_handler)

# Testing the subtract command
class TestSubtractCommand:
    def test_subtract(self,subtract_command,capsys):
        '''Testing multiply command'''            
        subtract_command.execute('4','2')
        captured=capsys.readouterr()
        assert "4 - 2 = 2" in captured.out

    def test_subtract_one_arg(self,subtract_command,capsys):
        '''Testing one argument'''
        subtract_command.execute('4')
        captured=capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_subtract_invalid_arg(self,subtract_command,capsys):
        '''Testing invalid argument'''
        subtract_command.execute('x','3')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_subtract_negative_numbers(self, subtract_command, capsys):
        '''Testing subtraction with negative numbers'''
        subtract_command.execute('-5', '3')
        captured = capsys.readouterr()
        assert "-5 - 3 = -8" in captured.out

    def test_subtract_error(self, subtract_command, capsys):
        '''Testing for invalid arguments'''
        with patch('app.plugins.subtractcommand.Calculator.subtract', side_effect=ValueError("Error")):
            subtract_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out

# End of program
