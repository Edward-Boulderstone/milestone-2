class Blackjack_Player:
    actions = ["hit", "stand"]

    def is_bust(self) -> bool:
        raise NotImplementedError

    def hit(self) -> None:
        raise NotImplementedError

    def stand(self) -> None:
        raise NotImplementedError

    def handle_turn(self) -> None:
        raise NotImplementedError

    def reset_for_next_game(self) -> None:
        raise NotImplementedError
