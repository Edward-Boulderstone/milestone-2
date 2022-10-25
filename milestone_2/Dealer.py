from milestone_2.Card import Card
from milestone_2.Deck import Deck
from milestone_2.Hand import Hand


class Dealer:
    instance = None

    def __new__(cls) -> "Dealer":
        if cls.instance is None:
            cls.instance = super(Dealer, cls).__new__(cls)
        return cls.instance

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

    def deal_starting_hand(self) -> Hand:
        """
        Returns: A starting hand for a game of blackjack
        """
        return Hand(self.deal_card(), self.deal_card())
