from app.commands import Command
from app.History.Managing_History import History_Manager

class SaveHistory(Command):
    def execute(self, *args):
        History_Manager.saving_history()