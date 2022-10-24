class Blackjack_Player:
    def is_bust(self) -> bool:
        raise NotImplementedError

    def hit(self) -> None:
        raise NotImplementedError

    def stand(self) -> None:
        raise NotImplementedError

    def handle_turn(self) -> None:
        raise NotImplementedError
