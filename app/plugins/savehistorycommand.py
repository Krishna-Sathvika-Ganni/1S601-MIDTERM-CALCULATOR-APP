from app.commands import Command,CommandHandler
from app.History.Facade_History import HistoryFacade 
import logging

logger=logging.getLogger(__name__)

class SaveHistory(Command):
    def __init__(self, command_handler=None):
        self.command_handler=command_handler
        self.history_facade=HistoryFacade()
        
    def execute(self):
        try:
            result = self.history_facade.save_history()
            if result:
                print(result)
            else:
                logger.info("No history to save")
                print("There is no history to save")
        except Exception as e:
            logger.error("Error")
            print(str(e))