from app.plugins.addcommand import Add
from app.plugins.subtractcommand import Subtract
from app.plugins.multiplycommand import Multiply
from app.plugins.dividecommand import Divide
from app.plugins.savehistorycommand import SaveHistory
from app.plugins.clearhistorycommand import ClearHistory
from app.plugins.loadhistorycommand import LoadHistory
from app.plugins.deletehistorycommand import DeleteHistory
from app.plugins.menucommand import Menu

class CommandFactory:

    _commands = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "savehistory": SaveHistory,
        "clearhistory": ClearHistory,
        "loadhistory": LoadHistory,
        "deletehistory": DeleteHistory,
        "menu": Menu,
    }
    
@staticmethod
def Create_Command(command_name, command_handler):
    command_class=CommandFactory._commands.get(command_name.lower())
    if command_class:
        return command_class(command_handler)
    raise ValueError("Unknown command")