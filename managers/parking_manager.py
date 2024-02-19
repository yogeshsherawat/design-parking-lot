from db.parking_lot_dao import ParkingLotDao


class ParkingManager(object):

    def __init__(self, space_finding_strategy):
        self.space_finding_strategy = space_finding_strategy

    def create_parking_lot(self, number_of_slots):
        ParkingLotDao.create_parking_lot(number_of_slots)

    def park_car(self, car):
        slot_number = self.space_finding_strategy.find_space()
        ParkingLotDao.mark_slot_used(car, slot_number)
        return slot_number

    def leave_slot(self, slot_number):
        ParkingLotDao.mark_slot_empty(slot_number)

    def get_parking_lot_status(self):
        n_slots = ParkingLotDao.get_n_slots()
        status = []
        for i in range(1, n_slots+1):
            if not ParkingLotDao.is_slot_empty(i):
                status.append((i, ParkingLotDao.get_car_in_slot(i)))
        return status


"""
open to extension, closed to modification
"""
