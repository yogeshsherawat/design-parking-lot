from validators import CommandValidator
from exceptions import InvalidCommand
from managers.parking_manager import ParkingManager
from command_executors import CreateParkingLotCommandExecutor, ParkCarCommandExecutor, LeaveCarCommandExecutor, ParkingLotStatusCommandExecutor
from outputters import Outputter
from strategy.space_finding import NearestSpaceFindingStrategy, SpaceFind

class CommandExecutorFactory:

    parking_manager = None
    outputter = None

    @staticmethod
    def init():
        if not CommandExecutorFactory.parking_manager:
            space_finding_strategy = NearestSpaceFindingStrategy()
            CommandExecutorFactory.parking_manager = ParkingManager(space_finding_strategy)
        if not CommandExecutorFactory.outputter:
            CommandExecutorFactory.outputter = Outputter()

    @staticmethod
    def get_command_executor(command):
        CommandExecutorFactory.init()
        if not CommandValidator.validate(command):
            raise InvalidCommand
        command_params = command.split(" ")
        command_name = command_params[0]
        if command_name == "create_parking_lot":
            return CreateParkingLotCommandExecutor(command, CommandExecutorFactory.parking_manager, CommandExecutorFactory.outputter)
        elif command_name == "park":
            return ParkCarCommandExecutor(command, CommandExecutorFactory.parking_manager, CommandExecutorFactory.outputter)
        elif command_name == "leave":
            return LeaveCarCommandExecutor(command, CommandExecutorFactory.parking_manager, CommandExecutorFactory.outputter)
        elif command_name == "status":
            return ParkingLotStatusCommandExecutor(command, CommandExecutorFactory.parking_manager, CommandExecutorFactory.outputter)
        else:
            raise InvalidCommand
