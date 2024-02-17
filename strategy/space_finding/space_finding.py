from ABC import ABC, abstractmethod


class SpaceFind(ABC):
    @abstractmethod
    def find_space(self, board):
        pass
