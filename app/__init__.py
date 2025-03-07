import inspect
import pkgutil
import importlib
from app.Factory.Command_Factory import CommandFactory
from app.commands import CommandHandler, Command
import logging
import sys
import os
import logging
import logging.config

logger=logging.getLogger(__name__)

class App:
    '''This is the App class'''

    def __init__(self, command=None):
        if command is None:
            command = CommandHandler()
        self.command_handler = command
        self.load_commands()
        os.makedirs('logs',exist_ok=True)
        self.configuring_logging()

    def configuring_logging(self):
        logging_conf_path='logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
            logger.info("Configured")
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
            logger.info("Logging configured")

    def load_commands(self):
        available_commands=["menu", "add", "subtract", "multiply", "divide", "savehistory", "loadhistory", "clearhistory", "deletehistory"]

        for cmd in available_commands:
            try:
                command_instance=CommandFactory.create_command(cmd, self.command_handler)
                self.command_handler.Register_Command(cmd, command_instance)
                logger.info(f"Command Registered is {cmd}")
            
            except ValueError:
                logger.warning(f"Umknown Command")

    # Here I have applied EAFP ( Easier to Ask for Forgiveness than Permission ) condition: Performs the operations and handles the errors if they occur
    def start(self):
        print("WELCOME TO THE CALCULATOR PROGRAM!!\n --> Type 'Menu' to see available commands. \n --> Type 'Exit' to quit.")
        while True:
            try:
                c = input("Enter the command: ").strip().lower()
                if c == "exit":
                    logger.info("Exited")
                    raise SystemExit("Program is Exiting..!")
                
                user_input_split = c.split()
                command_name = user_input_split[0]
                args = user_input_split[1:]

                command_name=command_name.lower()
                if not self.command_handler.Execute_Command(command_name, *args):
                    logger.warning(f"Unknown command: {command_name}")
                    print(f"Error: '{command_name}' is not a registered command")
            
            except Exception as e:
                logger.error("Error")
                print(f"An error occurred: {e}")
                