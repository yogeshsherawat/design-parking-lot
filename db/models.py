class Car:
    def __init__(self, registration_number, car_color):
        self.registration_number = registration_number
        self.car_color = car_color

    def get_registration_number(self):
        return self.registration_number

    def get_person_name(self):
        return self.car_color

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    def set_car_color(self, car_color):
        self.car_color = car_color

    def to_string(self):
        return self.registration_number + " " + self.car_color

class Slot:
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

