from milestone_2.Card import Card


class Hand:
    """
    A Hand object represents a player's hand in a game of Blackjack
    """

    def __init__(self, *cards: Card) -> None:
        self.hand = list(cards)

    def value(self) -> int:
        """
        Returns the Blackjack value of the hand
        """
        hand_value = sum(map(lambda card: card.get_value(), self.hand))
        aces_in_hand = self.ace_count()
        low_aces = 0
        while hand_value > 21 and low_aces < aces_in_hand:
            hand_value -= 10
            low_aces += 1

        return hand_value

    def is_bust(self) -> bool:
        """
        Returns the whether the hand is bust or not
        """
        return self.value() > 21

    def draw(self, card: Card) -> "Hand":
        """
        Adds a card to the hand
        """
        self.hand.append(card)
        return self

    def __eq__(self, other: object) -> bool:
        """
        Checks if this hand and another hand have the same blackjack value
        """
        if not isinstance(other, Hand):
            return NotImplemented
        if self.is_bust() and other.is_bust():
            return True
        if self.is_blackjack() and other.is_blackjack():
            return True
        if self.is_blackjack() or other.is_blackjack():
            return False
        return self.value() == other.value()

    def __gt__(self, other: object) -> bool:
        """
        Checks if current hand has greater blackjack value than another hand
        """
        if not isinstance(other, Hand):
            return NotImplemented
        if self.is_bust():
            return False
        if other.is_bust():
            return True
        if other.is_blackjack():
            return False
        if self.is_blackjack():
            return True
        return self.value() > other.value()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        """
        Checks if current hand has lesser blackjack value than another hand
        """
        return not (self == other or self > other)

    def is_blackjack(self) -> bool:
        """
        Checks if current hand is blackjack
        """
        return len(self.hand) == 2 and self.value() == 21

    def ace_count(self) -> int:
        """
        Returns count of aces in hand
        """
        return sum(map(lambda card: card.get_value() == 11, self.hand))

    def output(self, hidden: bool = False) -> str:
        """
        Outputs hand as string
        Args:
            hidden: boolean determining if only the first card is shown

        Returns:
            A user-friendly display of a blackjack hand
        """
        output = "Hand = {"
        for index in range(len(self.hand)):
            if hidden and index != 0:
                output += "*"
            else:
                output += str(self.hand[index])
            output += ", "

        output = output[:-2] + "}"
        if hidden:
            return output
        output += ", Value = "
        if self.is_blackjack():
            output += "Blackjack"
        else:
            output += str(self.value())

        return output
