from typing import List
from typing import Optional

from magic import Elements
from magic import Effect

DECK_SIZE = 108
POTENCY_LEVELS = 9
STARTING_HAND = 7


class Card:

    potency: int
    element: Optional[Elements]
    effect: Optional[Effect]

    def __init__(
        self,
        potency: int,
        element: Optional[Elements] = None,
        effect: Optional[Effect] = None
    ):
        self.potency = potency
        self.element = element
        self.effect = effect


class Deck:

    cards: List[Card]

    def __init__(self):
        self.cards = []

    def generate(self) -> None:

        # Number cards
        for element in Elements:
            self.cards.append(Card(0, element))
            for potency_level in range(1, POTENCY_LEVELS + 1):
                self.cards.extend([Card(potency_level, element), Card(potency_level, element)])


    def shuffle(self) -> None:
        pass
