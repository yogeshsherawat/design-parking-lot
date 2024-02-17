from .db import DB
from exceptions import CarNotPresentInParking


class ParkingLotDao(object):

    @staticmethod
    def get_parking_space_by_registration_number(registration_number):
        sequence_number = DB.get_parking_space_by_registration_number(registration_number)
        if not sequence_number:
            raise CarNotPresentInParking()
        return sequence_number

    @staticmethod
    def get_empty_spaces():
        return DB.get_empty_spaces()
