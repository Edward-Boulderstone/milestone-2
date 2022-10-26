from milestone_2.Dealer import Dealer


class Blackjack_Player:
    actions = ["hit", "stand"]

    def __init__(self):
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
        raise NotImplementedError

    def reset_for_next_game(self) -> None:
        self.hand = Dealer().deal_starting_hand()

    def can_perform_actions(self) -> bool:
        return not (self.hand.is_bust() or self.is_stood)

    def display_hand(self) -> str:
        return self.hand.output()
