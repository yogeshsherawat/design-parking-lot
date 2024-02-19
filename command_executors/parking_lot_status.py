
from .command_exectuor import CommandExecutor

class ParkingLotStatusCommandExecutor(CommandExecutor):
    def __init__(self, command, parking_manager, outputter):
        self.command = command
        self.parking_manager = parking_manager
        self.outputter = outputter

    def execute(self):
        status = self.parking_manager.get_parking_lot_status()
        self.outputter.output(status)