'''The test_calculation.py module contains tests for the calculator operations and calculation class'''

# pylint: disable=unnecessary-dunder-call, invalid-name

from decimal import Decimal
from app.calculator.calculation import Calculation
from app.operation.operations import add

def test_calculation_operations(x, y, operation, expected):
    '''Calculation operations with various cases'''
    calc = Calculation(x, y, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {x} and {y}"

def test_calculation_repr():
    '''Test the string representation (__repr__) of the Calculation class.'''
    calc=Calculation(Decimal('3'), Decimal('4'), add)
    expected_repr="Calculation(3, 4, add)"
    assert repr(calc) == expected_repr, "The __repr__ method is not matching the expected string."

# End of program
