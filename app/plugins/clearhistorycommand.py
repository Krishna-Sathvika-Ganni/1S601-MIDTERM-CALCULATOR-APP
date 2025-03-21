from app.commands import Command,CommandHandler
from app.History.Facade_History import HistoryFacade 
import logging

logger=logging.getLogger(__name__)

class ClearHistory(Command):
    def __init__(self, command_handler=None):
        self.command_handler=command_handler
        self.history_facade=HistoryFacade()
        
    def execute(self):
        try:
            result = self.history_facade.clear_history()
            if result:
                print(result)
            else:
                logger.info("Cleared")
                print("History cleared successfully")
        except Exception as e:
            print(str(e))