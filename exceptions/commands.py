class InvalidCommand(Exception):
    def __init__(self):
        self.message = f"Invalid command Provided"
