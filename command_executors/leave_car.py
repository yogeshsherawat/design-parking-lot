from .command_exectuor import CommandExecutor


class LeaveCarCommandExecutor(CommandExecutor):

    def __init__(self, command, parking_manager, outputter):
        self.command = command
        self.parking_manager = parking_manager
        self.outputter = outputter

    def execute(self):
        [command_name, slot_number] = self.command.split(" ")
        slot_number = int(slot_number)
        self.parking_manager.leave_slot(slot_number)
        self.outputter.output(f"Slot number {slot_number} is free")