from app.commands import Command,CommandHandler
from app.History.Managing_History import History_Manager

class SaveHistory(Command):
    def __init__(self, command_handler=None):
        self.command_handler=command_handler
        
    def execute(self):
        History_Manager.saving_history()