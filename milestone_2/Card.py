from milestone_2.Card_Values import suits
from milestone_2.Card_Values import face_values
from milestone_2.Card_Values import face_value_to_numerical_value


class Card:
    """
    A Card object represents a playing card from a 52 card tarot deck
    """

    def __init__(self, suit: str, value: int) -> None:
        assert suit in suits
        assert value in range(1, len(face_values) + 1)
        self.suit = suit
        self.face_value = face_values[value - 1]

    def get_value(self) -> int:
        """
        returns Blackjack value of this card
        """
        return face_value_to_numerical_value[self.face_value]

    def __eq__(self, other: object) -> bool:
        """
        Compares two cards to check if they have the same values
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.face_value == other.face_value

    def __hash__(self):
        return hash(self.suit) * hash(self.face_value)

    def __str__(self) -> str:
        """
        Returns: string display of Card
        """
        return f"{self.face_value} of {self.suit}s"
