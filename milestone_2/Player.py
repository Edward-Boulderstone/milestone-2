from milestone_2.Blackjack_Player import Blackjack_Player
from milestone_2.Dealer import Dealer
from milestone_2.Hand import Hand
from milestone_2.Wallet import Wallet


class Player(Blackjack_Player):
    def __init__(self):
        self.wallet = Wallet()
        self.hand = Dealer().deal_starting_hand()
        self.is_stood = False

    def is_bust(self) -> bool:
        return self.hand.is_bust()

    def hit(self) -> None:
        if not self.can_perform_actions():
            return
        self.hand.draw(Dealer().deal_card())

    def stand(self) -> None:
        if not self.can_perform_actions():
            return
        self.is_stood = True

    def handle_turn(self) -> None:
        if not self.can_perform_actions:
            return
        if self.user_input().lower() == "hit":
            return self.hit()
        return self.stand()

    def reset_for_next_game(self) -> None:
        self.hand = Dealer().deal_starting_hand()

    def can_perform_actions(self) -> bool:
        return not (self.hand.is_bust() or self.is_stood)

    def user_input(self) -> str:
        user_input = ""
        while user_input.lower() not in self.actions:
            user_input = input(
                f"Please choose one of the following game actions {self.actions}"
            )
        return user_input
