from app.commands import Command
from app.History.Managing_History import History_Manager

class ClearHistory(Command):
    def execute(self,*args):
        History_Manager.clear_history()