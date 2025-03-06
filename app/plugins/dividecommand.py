from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command
import logging

logger=logging.getLogger(__name__)

class Divide(Command):
    '''This is the divide command class'''
    def __init__(self, command_handler):
        self.command_handler=command_handler
        
    def execute(self, *args):
        if not args:  # This prompts for input, if arguments are not given
            logger.info("There are no arguments given, so prompting for input")
            args = input("Enter two numbers separated by space: ").split()
        if len(args) != 2:  # Makes sure that only two arguments must be given
            logger.error("Number of arguments given is incorrect")
            print("Only two arguments must be given")
            return

        try:
            x, y = map(Decimal, args) 
            if y==0:
                logger.error("Division by zero cannot be done")
                print("Cannot be divided by zero") # We can't divide by zero which raises a error
                return 
            result = Calculator.divide(x, y)
            logger.info("Division operation is being done")
            print(f"{x} / {y} = {result}")
        except InvalidOperation:
            logger.error("Invalid arguments given")
            print(f"One of the entered numbers is invalid. Please enter valid inputs.")
        except ValueError as ve:  
            logger.error("Value error occured")
            print(f"{ve}")
        except Exception as e:
            logger.error("Unexpected error")
            print(f"{e}")