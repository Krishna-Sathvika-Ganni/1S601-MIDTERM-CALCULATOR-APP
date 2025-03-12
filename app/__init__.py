from app.Factory.Command_Factory import CommandFactory
from app.commands import CommandHandler
import logging
import os
import logging
import logging.config
from dotenv import load_dotenv
from config import CONFIG 

logger=logging.getLogger(__name__)

class App:
    '''This is the App class'''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
            cls._instance.initialized=False
        return cls._instance

    def __init__(self, command=None):
        if not self.initialized:
            if command is None:
                self.command_handler = CommandHandler()
            else:
                self.command_handler = command
        self.load_commands()
        os.makedirs('logs',exist_ok=True)
        self.configuring_logging()
        load_dotenv()
        self.initialized=True

        logger.info(f"App initialized with environment: {CONFIG['environment']}")
        logger.info(f"Log level set to: {CONFIG['log_level']}")

    def configuring_logging(self):
        logging_conf_path='logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
            logger.info("Configured")
        else:
            level = getattr(logging, CONFIG['log_level'].upper(), logging.INFO)
            logging.basicConfig(
                level=level, 
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler('logs/app.log'),
                    logging.StreamHandler()
                ]
            )
            logger.info("Logging configured")


    def load_commands(self):
        available_commands=["menu", "add", "subtract", "multiply", "divide", "savehistory", "loadhistory", "clearhistory", "deletehistory"]

        for cmd in available_commands:
            try:
                command_instance=CommandFactory.create_command(cmd, self.command_handler)
                self.command_handler.register_command(cmd, command_instance)
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
                if not self.command_handler.execute_command(command_name, *args):
                    logger.warning(f"Unknown command: {command_name}")
                    print(f"Error: '{command_name}' is not a registered command")
            
            except Exception as e:
                logger.error("Error")
                print(f"An error occurred: {e}")
                