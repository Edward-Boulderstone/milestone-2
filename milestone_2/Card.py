suits = ("Spade", "Club", "Heart", "Diamond")
face_values = (
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
)


class Card:
    def __init__(self, suit: str, value: int):
        assert suit in suits
        assert value in range(14)
        self.suit = suit
        self.face_value = face_values[value - 1]
