from app.commands import Command
from app.History.Managing_History import History_Manager

class LoadHistory(Command):
    def execute(self, *args):
        History_Manager.load_history()