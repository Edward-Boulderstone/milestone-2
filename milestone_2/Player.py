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
        """
        Allows user to place bets by spending funds
        Args:
            funds_to_bet: funds to bet
        """
        self.wallet.spend(funds_to_bet)

    def add_funds(self, funds_to_add: int) -> None:
        """
        Allows user to gain funds from winning bets
        Args:
            funds_to_add: Funds to be rewarded
        """
        self.wallet.add_funds(funds_to_add)
