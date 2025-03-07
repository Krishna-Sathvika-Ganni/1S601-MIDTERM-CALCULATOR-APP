from app.commands import Command,CommandHandler
from app.History.Facade_History import HistoryFacade 

class SaveHistory(Command):
    def __init__(self, command_handler=None):
        self.command_handler=command_handler
        self.history_facade=HistoryFacade()
        
    def execute(self):
        self.history_facade.save_history()