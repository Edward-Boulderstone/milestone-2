from milestone_2.Blackjack_Player import Blackjack_Player
from milestone_2.Hand import Hand


class Dealer_AI(Blackjack_Player):
    minimum_value = 17

    def __init__(self):
        super().__init__()
        self.hand_to_beat = Hand()

    def set_target_hand(self, target_to_beat: Hand) -> None:
        self.hand_to_beat = target_to_beat

    def need_to_hit(self):
        """
        Determined by a minimum value, and the dealer needs to try to beat the player's hand
        Blackjacks are unbeatable
        Returns: Whether the dealer AI needs to hit or not
        """
        if self.hand_to_beat.is_blackjack():
            return False
        return self.hand.value() < self.minimum_value or self.hand < self.hand_to_beat

    def can_perform_actions(self) -> bool:
        """
        The AI cannot perform actions when it is bust, stood, or a target hand has not been set
        """
        return not (
            self.hand.is_bust() or self.is_stood or self.hand_to_beat.value() == 0
        )

    def handle_turn(self) -> None:
        """
        Handles the calling of functions for the AI class
        """
        if self.need_to_hit() and self.can_perform_actions():
            self.hit()
        else:
            self.stand()

    def display_hand_hidden(self) -> str:
        """
        Displays the dealer's hand when the user is making actions
        """
        return self.hand.output(True)
