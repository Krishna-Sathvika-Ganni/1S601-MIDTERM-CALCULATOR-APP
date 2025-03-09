from Strategy_app.strategies import Command_strategy
from Strategy_app.strategies.addcommand import Add
from Strategy_app.strategies.subtractcommand import Subtract
from Strategy_app.strategies.multiplycommand import Multiply
from Strategy_app.strategies.dividecommand import Divide

class App:
    def __init__(self):
        self.command = None  

    def set_command(self, command: Command_strategy):
        self.command = command

    def execute_command(self, *args):
        if self.command is None:
            raise ValueError("Command strategy not set.")
        return self.command.execute(*args)

    def start(self):
        print("This is the Calculator Program using the Strategy Pattern!\n")

        while True:
            try:
                user_input = input("Enter command (add/subtract/multiply/divide) followed by numbers: ").strip().lower()
                if user_input == 'exit':
                    print("Exiting...")
                    break

                parts = user_input.split()
                command_name = parts[0]
                args = parts[1:]

                # Choose strategy based on user input
                if command_name == 'add':
                    self.set_command(Add())
                elif command_name == 'subtract':
                    self.set_command(Subtract())
                elif command_name == 'multiply':
                    self.set_command(Multiply())
                elif command_name == 'divide':
                    self.set_command(Divide())
                else:
                    print("Unknown command.")
                    continue

                result = self.execute_command(*args)
                print(f"Result: {result}")

            except Exception as e:
                print(f"Error: {e}")
