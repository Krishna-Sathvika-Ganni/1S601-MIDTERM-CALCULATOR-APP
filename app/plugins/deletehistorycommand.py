from app.commands import Command
from app.History.Managing_History import History_Manager

def DeleteHistory(Command):
    def execure(self,*args):
        History_Manager.delete_history()