from milestone_2.Blackjack_Player import Blackjack_Player
from milestone_2.Wallet import Wallet


class Player(Blackjack_Player):
    def __init__(self):
        super().__init__()
        self.wallet = Wallet()

    def handle_turn(self) -> None:
        if not self.can_perform_actions:
            return
        if self.user_input().lower() == "hit":
            return self.hit()
        return self.stand()

    def user_input(self) -> str:
        user_input = ""
        while user_input.lower() not in self.actions:
            user_input = input(
                f"Please choose one of the following game actions {self.actions}"
            )
        return user_input

    def get_funds(self):
        return self.wallet.funds

    def bet_funds(self, funds_to_bet: int) -> None:
        pass

    def add_funds(self, funds_to_add: int) -> None:
        pass
