from strategies import Command_strategy

class Divide(Command_strategy):
    def execute(self, *args):
        try:
            result = int(args[0])
            for arg in args[1:]:
                result /= int(arg)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"