
from .mode import Mode


class InteractiveMode(Mode):

    def process(self):
        while True:
            command = input("Enter command: ")
            if command == "exit":
                break
            self.process_command(command)
