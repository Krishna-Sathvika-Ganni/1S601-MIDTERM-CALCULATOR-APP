from app.commands import Command
import logging

logger=logging.getLogger(__name__)

class Menu(Command):
    '''This displays available commands in the system'''
   
    def __init__(self, command_handler):
        self.command_handler=command_handler

    def execute(self, *args):
        commands=self.command_handler.get_registered_commands()

        if not commands:
            logger.warning("No commands")
            print("There are no commands")
            return
        logger.info("Available commands")
        print("Commands Available:")
        for command in commands:
            print(f"-> {command}") 
        print("Type 'exit' to quit" )