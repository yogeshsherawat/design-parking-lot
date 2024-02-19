
from .mode import Mode


class FileMode(Mode):
    def __init__(self, file_path):
        self.file_path = file_path

    def process(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                self.process_command(line.strip())