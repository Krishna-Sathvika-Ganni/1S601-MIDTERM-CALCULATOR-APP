from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command
import logging

logger=logging.getLogger(__name__)

class Add(Command):
    '''This is the add command class'''
    def __init__(self, command_handler):
        self.command_handler=command_handler
        
    def execute(self, *args):
        if not args:  
            # This prompts for input, if arguments are not given.
            args = input("Enter two numbers: ").split()
            logger.info("There are no arguments given, so prompting for input")
        if len(args) != 2:  
            # Makes sure that only two arguments must be given
            print("Only two arguments must be given")
            logger.error("Number of arguments given is incorrect")
            return

        try:
            x, y = map(Decimal, args)  
            result = Calculator.add(x, y)
            print(f"{x} + {y} = {result}")
            logger.info("Addition operation is being done")
        
        except InvalidOperation:
            logger.error("Invalid arguments given")
            print(f"One of the entered numbers is invalid. Please enter valid inputs.")
        
        except ValueError as ve: 
            logger.error("Value error occured")
            print(f"{ve}")
        
        except Exception as e:
            logger.error("Unexpected error")
            print(f"{e}")