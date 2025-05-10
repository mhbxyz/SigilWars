from abc import ABC
from abc import abstractmethod
from enum import StrEnum


class Elements(StrEnum):
    Red = "Fire"
    Blue = "Water"
    Green = "Earth"
    Purple = "Arcane"


class Effect(ABC):

    name: str
    description: str

    @abstractmethod
    def apply():
        pass


class Spell(Effect):
    pass


class Rule(Effect):
    pass
