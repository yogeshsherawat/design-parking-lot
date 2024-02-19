from .db import DB
from exceptions import CarNotPresentInParking


class ParkingLotDao(object):

    @staticmethod
    def get_n_slots():
        return len(DB.slot_to_car_dict)

    @staticmethod
    def is_slot_empty(slot):
        return DB.slot_to_car_dict[slot] is None

    @staticmethod
    def create_parking_lot(n_lots):
        for i in range(1, n_lots+1):
            DB.slot_to_car_dict[i] = None

    @staticmethod
    def mark_slot_used(car, slot):
        DB.slot_to_car_dict[slot] = car

    @staticmethod
    def mark_slot_empty(slot):
        DB.slot_to_car_dict[slot] = None

    @staticmethod
    def get_car_in_slot(slot):
        car = DB.slot_to_car_dict[slot]
        if car is None:
            raise CarNotPresentInParking
        return car.to_string()


