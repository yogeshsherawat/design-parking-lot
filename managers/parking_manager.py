from db.parking_lot_dao import ParkingLotDao
from exceptions import CarAlreadyPresentInParking


class ParkingManager(object):

    def __init__(self, space_finding_strategy):
        self.space_finding_strategy = space_finding_strategy

    def park_car(self, registration_number):
        parking_space_sequence_number = ParkingLotDao.get_parking_space_by_registration_number(registration_number)
        if parking_space_sequence_number:
            raise CarAlreadyPresentInParking()
        parking_space_sequence_number = self.space_finding_strategy.find_space()
        ParkingLotDao.mark_parking_space(parking_space_sequence_number, registration_number)
        return parking_space_sequence_number
