class Car:
    def __init__(self, registration_number, person_name):
        self.registration_number = registration_number
        self.person_name = person_name

    def get_registration_number(self):
        return self.registration_number

    def get_person_name(self):
        return self.person_name

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    def set_person_name(self, person_name):
        self.get_person_name = person_name


class ParkingSpace:
    def __init__(self, sequence_number):
        self.sequence_number = sequence_number
        self.car = None

    def get_sequence_number(self):
        return self.sequence_number

    def set_sequence_number(self, sequence_number):
        self.sequence_number = sequence_number

    def get_car(self):
        return self.car

    def set_car(self, car):
        self.car = car

