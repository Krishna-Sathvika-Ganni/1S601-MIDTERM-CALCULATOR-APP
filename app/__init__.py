import inspect
import pkgutil
import importlib
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
        self.load_plugins()  # This automatically loads the plugins
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

    # Here I have applied EAFP ( Easier to Ask for Forgiveness than Permission ) condition: Performs the operations and handles the errors if they occur
    def load_plugins(self):
        '''This dynamically loads the plugins'''
        plugins_package = "app.plugins"  
        for _, plugin_name, _ in pkgutil.iter_modules([plugins_package.replace(".","/")]):  
            try:
                plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                logger.info("Attempting to load plugin")
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                        init_signature=inspect.signature(item.__init__)
                        if len(init_signature.parameters)>1:
                            if plugin_name.replace("_command", "") not in self.command_handler.commands:
                                self.command_handler.Register_Command(plugin_name.replace("command", "").strip("_"), item(self.command_handler))
                        else:
                            if plugin_name.replace("_command", "") not in self.command_handler.commands:
                                self.command_handler.Register_Command(plugin_name.replace("command", "").strip("_"), item())
            
            except Exception as e:
                logger.error("Failed to load plugin")
                print(f"Failed to load plugin {plugin_name}: {e}")

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
                