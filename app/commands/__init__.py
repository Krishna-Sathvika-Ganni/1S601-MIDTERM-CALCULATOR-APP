# disable=trailing-whitespace, missing-final-newline, missing-docstring
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Command(ABC):
    '''This is the abstract base for commands.'''
    @abstractmethod
    def execute(self,*args):
        pass

class CommandHandler:
    '''This is the CommandHandler class.'''
    def __init__(self):
        self.commands={}
    
    def register_command(self, command_name: str, command: Command):
        '''This function registers a command.'''
        if command_name in self.commands:
            logger.warning(f"Command '{command_name}' is already registered.")
        else:
            logger.info(f"Registering command: {command_name}")
        self.commands[command_name] = command
    
    # Here is also LBYL condition is applied: we check whether the command is registered or not before executing
    def execute_command(self, command_name: str, *args):
        '''Executes a registered command if exists'''
        if command_name in self.commands:
            try:
                logger.info(f"Executing: {command_name}")
                self.commands[command_name].execute(*args)
                return True
            
            except Exception as e:
                logging.error(f"Error executing: {command_name}: {e}")
        else:
            logger.error(f"Command {command_name} not found")
            return False

    def get_registered_commands(self):
        '''Gives the list of registered commands'''
        if self.commands:
            logger.info(f"Commands registered: {','.join(self.commands.keys())}")
            return list(self.commands.keys())
        else:
            logger.warning("There are no commands")
            return []