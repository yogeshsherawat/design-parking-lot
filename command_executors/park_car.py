from .command_exectuor import CommandExecutor
from db.models import Car


class ParkCarCommandExecutor(CommandExecutor):

    def __init__(self, command, parking_manager, outputter):
        self.command = command
        self.parking_manager = parking_manager
        self.outputter = outputter

    def execute(self):
        [command_name, reg_no, car_color] = self.command.split(" ")
        car = Car(reg_no, car_color)
        slot_number = self.parking_manager.park_car(car)
        self.outputter.output(
            f"Car with registration number {car.get_registration_number()} is parked at space {slot_number}")
