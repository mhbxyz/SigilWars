from typing import List
from enum import Enum

from cards import Card


class TurnAction(Enum):
    pass


class Player:

    name: str
    hand: List[Card]

    def __init__(self, name: str) -> None:
        self.name = name


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=Singleton):

    players: List[Player]
    turn_index: int

    def __init__(self) -> None:
        self.turn_index = 0

    def loop(self) -> None:
        pass
