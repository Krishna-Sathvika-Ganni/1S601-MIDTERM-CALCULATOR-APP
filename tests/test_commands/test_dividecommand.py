# pylint: disable=missing-class-docstring
'''This is test_command file'''
from unittest.mock import Mock, patch
import pytest
from app.plugins.dividecommand import Divide

@pytest.fixture
def mock_command_handler():
    '''Mock_command_handler'''
    mock_handler=Mock()
    mock_handler.Register_Command=Mock()
    mock_handler.Execute_Command=Mock()
    return mock_handler

@pytest.fixture
def divide_command(mock_command_handler):
    '''Fixture'''
    return Divide(command_handler=mock_command_handler)

class TestDivideCommand:
    '''Testing the Divide command'''
    def test_Divide(self,divide_command,capsys):
        '''Testing Divide command'''
        divide_command.execute('4','2')
        captured=capsys.readouterr()
        assert "4 / 2 = 2" in captured.out

    def test_Divide_one_arg(self,divide_command,capsys):
        '''Testing one argument'''
        divide_command.execute('4')
        captured=capsys.readouterr()

        assert "Only two arguments must be given" in captured.out


    def test_Divide_invalid_arg(self,divide_command,capsys):
        '''Testing invalid argument'''
        divide_command.execute('x','3')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_Divide_by_zero(self,divide_command,capsys):
        '''Testing divide by zero'''
        divide_command.execute('9','0')
        captured=capsys.readouterr()
        assert "Cannot be divided by zero" in captured.out

    def test_divide_error(self, divide_command, capsys):
        '''Testing for invalid arguments'''

        with patch('app.plugins.dividecommand.Calculator.divide', side_effect=ValueError("Error")):

            divide_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out

# End of program
