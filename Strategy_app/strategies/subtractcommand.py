from strategies import Command_strategy

class Subtract(Command_strategy):
    def execute(self, *args):
        return int(args[0]) - sum(map(int, args[1:]))