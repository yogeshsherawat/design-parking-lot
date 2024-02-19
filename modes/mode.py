from abc import ABC, abstractmethod
from factory.command import CommandExecutorFactory
from exceptions import InvalidCommand
from outputters import Outputter


class Mode(ABC):

    def __init__(self):
        self.outputter = Outputter()


    def process_command(self, command):
        try:
            command_executer = CommandExecutorFactory.get_command_executor(command)
        except InvalidCommand:
            self.outputter.output("Invalid command")
            return
        command_executer.execute()

    @abstractmethod
    def process(self):
        pass
