from milestone_2.Card import Card
from milestone_2.Deck import Deck


class Dealer:
    def __init__(self):
        self.deck = Deck()

    def deal_card(self) -> Card:
        """
        Draws and deals a card from a deck, if there are no cards in a deck, a new one is created
        Returns: Random card from a deck

        """
        try:
            return self.deck.draw()
        except AssertionError:
            self.deck = Deck()
        return self.deck.draw()

    def deal_starting_hand(self) -> tuple[Card, Card]:
        """
        Returns: A starting hand for a game of blackjack
        """
        return self.deal_card(), self.deal_card()
