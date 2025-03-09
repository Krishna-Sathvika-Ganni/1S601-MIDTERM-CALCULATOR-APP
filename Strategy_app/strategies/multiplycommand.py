from strategies import Command_strategy 

class Multiply(Command_strategy):
    def execute(self, *args):
        result = 1
        for arg in args:
            result *= int(arg)
        return result