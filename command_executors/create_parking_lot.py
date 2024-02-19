from .command_exectuor import CommandExecutor
from managers import ParkingManager


class CreateParkingLotCommandExecutor(CommandExecutor):
    def __init__(self, command, parking_manager, outputter):
        self.command = command
        self.parking_manager = parking_manager
        self.outputter = outputter

    def execute(self):
        [command_name, number_of_slots] = self.command.split(" ")
        number_of_slots = int(number_of_slots)
        self.parking_manager.create_parking_lot(number_of_slots)
        self.outputter.output(f"Created Parking Lot with {number_of_slots} slots")



