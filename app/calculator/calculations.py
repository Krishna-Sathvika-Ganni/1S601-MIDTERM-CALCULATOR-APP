from decimal import Decimal
from typing import Callable
from typing import List
from app.calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    '''Used the class method'''
    
    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history
    
    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        return [cal for cal in cls.history if cal.operation.__name__ == operation_name]