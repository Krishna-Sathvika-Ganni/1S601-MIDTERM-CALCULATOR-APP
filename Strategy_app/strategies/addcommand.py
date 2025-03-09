from strategies import Command_strategy

class Add(Command_strategy):
    def execute(self, *args):
        return sum(map(int, args))
