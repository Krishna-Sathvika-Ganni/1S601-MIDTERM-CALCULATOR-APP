from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command
import logging

logger=logging.getLogger(__name__)

class Multiply(Command):
    '''This is the Multiply command class'''
    def __init__(self, command_handler):
        self.command_handler=command_handler

    def execute(self, *args):
        if not args:  # This prompts for input, if arguments are not given
            logger.info("There are no arguments given, so prompting for input")
            args = input("Enter two numbers: ").split()
        if len(args) != 2:  # Makes sure that only two arguments must be given
            logger.error("Number of arguments given is incorrect")
            print("Only two arguments must be given")
            return
        
        # Here I have applied EAFP ( Easier to Ask for Forgiveness than Permission ) condition: Performs the operations and handles the errors if they occur
        try:
            x, y = map(Decimal, args)  
            result = Calculator.multiply(x, y)
            logger.info("Multiplication operation is being done")
            print(f"{x} x {y} = {result}")
        except InvalidOperation:
            logger.error("Invalid arguments given")
            print(f"One of the entered numbers is invalid. Please enter valid inputs.")
        except ValueError as ve: 
            logger.error("Value error occured") 
            print(f"{ve}")
        except Exception as e:
            logger.error("Unexpected error")
            print(f"{e}")