from app.operation.operations import add, subtract # Imported add, subtract
from app.calculator.calculation import Calculation
from app.calculator.calculations import Calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    '''Created the class Calculator'''

    '''Used Static method'''

    @staticmethod
    def _perform_operation(x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation=Calculation.create(x, y, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(x: Decimal,y: Decimal) -> Decimal:
        return Calculator._perform_operation(x, y, add)
    
    @staticmethod
    def subtract(x: Decimal,y: Decimal) -> Decimal:
        return Calculator._perform_operation(x, y, subtract)
    