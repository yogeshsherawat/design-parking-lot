class CarNotPresentInParking(Exception):
    def __init__(self):
        self.message = "Car not present in parking"


class ParkingFullException(Exception):
    def __init__(self):
        self.message = "Parking Full"


class ParkingSpaceNotAvailableException(Exception):
    def __init__(self):
        self.message = "Parking Space Not Available"

class CarAlreadyPresentInParking(Exception):
    def __init__(self):
        self.message = "Car already present in parking"