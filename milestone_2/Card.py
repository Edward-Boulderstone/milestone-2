from Card_Values import suits
from Card_Values import face_values


class Card:
    """
    A Card object represents a playing card from a 52 card tarot deck
    """

    def __init__(self, suit: str, value: int):
        assert suit in suits
        assert value in range(len(face_values))
        self.suit = suit
        self.face_value = face_values[value - 1]
