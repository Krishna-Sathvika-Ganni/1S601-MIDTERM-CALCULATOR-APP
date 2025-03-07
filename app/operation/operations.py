from decimal import Decimal

def add(x: Decimal, y: Decimal) -> Decimal:
    return x + y

def subtract(x: Decimal,y: Decimal) -> Decimal:
    return x - y

def multiply(x: Decimal,y: Decimal) -> Decimal:
    return x * y

# Here LBYL(Look Before You Leap condition ) is applied: we check whether the second number is zero or not before dividing
def divide(x: Decimal,y: Decimal) -> Decimal:
    if y == Decimal('0'):
        raise ValueError("Cannot be divided by Zero")
    return x / y