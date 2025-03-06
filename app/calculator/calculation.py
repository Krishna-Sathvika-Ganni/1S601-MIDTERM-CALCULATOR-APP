from app.operation.operations import add, subtract,multiply # Imported the add, subtract operations from operations 
from decimal import Decimal
from typing import Callable

class Calculation:
    '''Created a class calculation'''
    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.x = x
        self.y = y
        self.operation = operation

    '''Used static method to define a method within a class'''
    
    @staticmethod
    def create(x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(x, y, operation)
    
    def perform(self) -> Decimal:
        return self.operation(self.x, self.y)
    
    def __repr__(self):
        return f"Calculation({self.x}, {self.y}, {self.operation.__name__})"