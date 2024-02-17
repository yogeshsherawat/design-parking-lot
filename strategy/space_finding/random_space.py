from random import randint
from db.parking_lot_dao import ParkingLotDao
from .space_finding import SpaceFind


class RandomSpaceFindingStrategy(SpaceFind):
    def __init__(self, space):
        self.name = "Random Space Finding Strategy"

    def find_space(self):
        all_spaces = ParkingLotDao.get_empty_spaces()
        return all_spaces[randint(0, len(all_spaces) - 1)]
