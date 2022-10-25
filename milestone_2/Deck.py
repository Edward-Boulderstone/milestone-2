from random import shuffle
from milestone_2.Card import Card
from milestone_2.Card_Values import suits, face_values


class Deck:
    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for face_value in range(1, len(face_values) + 1):
                self.deck.append(Card(suit, face_value))
        shuffle(self.deck)

    def draw(self) -> Card:
        """
        Draws and returns a card from the deck
        Returns: a card from the deck
        """
        assert len(self.deck) > 0
        return self.deck.pop()
