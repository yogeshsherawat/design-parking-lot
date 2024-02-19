from random import randint
from db.parking_lot_dao import ParkingLotDao
from .space_finding import SpaceFind


class NearestSpaceFindingStrategy(SpaceFind):
    def __init__(self):
        self.name = "Nearest Space Finding Strategy"

    def find_space(self):
        n_slots = ParkingLotDao.get_n_slots()
        for i in range(1, n_slots+1):
            if ParkingLotDao.is_slot_empty(i):
                return i
