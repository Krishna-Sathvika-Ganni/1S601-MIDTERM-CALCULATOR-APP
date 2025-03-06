from app.commands import Command,CommandHandler
from app.History.Managing_History import History_Manager

def DeleteHistory(Command):
    def __init__(self, command_handler=None):
        self.command_handler=command_handler
        
    def execure(self):
        History_Manager.delete_history()