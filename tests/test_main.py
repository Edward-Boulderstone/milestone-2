from unittest.mock import patch
from milestone_2.main import introduce_game


@patch("builtins.print")
def test_display_welcome_message(mock_print) -> None:
    """
    Tests that the user is shown a welcome message when the game is started
    """
    introduce_game()
    mock_print.assert_any_call("Blackjack")
    mock_print.assert_any_call(
        "Try to beat the dealer by getting your hand to as close as 21 as possible, "
        "but not over"
    )


@patch("milestone_2.Blackjack_Game.initialize_game")
def test_initializes_game_and_runs_it(blackjack_initialize_game) -> None:
    """
    Tests that the game is initialised and ran following running the main file
    """
    introduce_game()
    blackjack_initialize_game.assert_called_once_with()
