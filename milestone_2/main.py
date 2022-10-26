from milestone_2 import Blackjack_Game


def introduce_game() -> None:
    """
    Introduces the game to the player, and then calls the game handler to initialize
    """
    print("Blackjack")
    print(
        "Try to beat the dealer by getting your hand to as close as 21 as possible, "
        "but not over"
    )
    Blackjack_Game.initialize_game()


if __name__ == "__main__":
    introduce_game()
