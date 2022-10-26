from unittest.mock import patch
from _pytest.fixtures import fixture

from milestone_2.Blackjack_Player import Blackjack_Player
from milestone_2.End_Of_Game import handle_end_of_game, win, push, loss
from milestone_2.Player import Player
from milestone_2.Wallet import Wallet


class Player_Stub(Player):
    def __init__(self):
        super().__init__()
        self.funds_added = 0

    def add_funds(self, funds_to_add: int) -> None:
        self.funds_added += funds_to_add


@fixture
def player_stub() -> Player:
    return Player_Stub()


@fixture
def dealer_stub() -> Blackjack_Player:
    return Blackjack_Player()


@fixture
def wallet() -> Wallet:
    return Wallet()


@patch("milestone_2.End_Of_Game.win")
@patch("milestone_2.End_Of_Game.push")
@patch("milestone_2.End_Of_Game.loss")
@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: False,
)
@patch("milestone_2.Hand.Hand.__gt__", lambda *args: True)
@patch("milestone_2.Hand.Hand.__eq__", lambda *args: False)
def test_correct_identification_of_player_victory(
    mock_loss, mock_push, mock_win, player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when the user's hand is worth more than the dealer's and neither can take any actions,
    the win method will be called
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    handle_end_of_game(player_stub, dealer_stub, 0)
    mock_win.assert_called_with(player_stub, 0)
    mock_push.assert_not_called()
    mock_loss.assert_not_called()


@patch("milestone_2.End_Of_Game.win")
@patch("milestone_2.End_Of_Game.push")
@patch("milestone_2.End_Of_Game.loss")
@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: False,
)
@patch("milestone_2.Hand.Hand.__gt__", lambda *args: False)
@patch("milestone_2.Hand.Hand.__eq__", lambda *args: True)
def test_correct_identification_of_push(
    mock_loss, mock_push, mock_win, player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when the user's hand is worth the same as the dealer's and neither can take any actions,
    the push method will be called
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    handle_end_of_game(player_stub, dealer_stub, 0)
    mock_win.assert_not_called()
    mock_push.assert_called_with(player_stub, 0)
    mock_loss.assert_not_called()


@patch("milestone_2.End_Of_Game.win")
@patch("milestone_2.End_Of_Game.push")
@patch("milestone_2.End_Of_Game.loss")
@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: False,
)
@patch("milestone_2.Hand.Hand.__gt__", lambda *args: False)
@patch("milestone_2.Hand.Hand.__eq__", lambda *args: False)
def test_correct_identification_of_player_loss(
    mock_loss, mock_push, mock_win, player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when the dealer's hand is worth more than the user's and neither can take any actions,
    the loss method will be called
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    handle_end_of_game(player_stub, dealer_stub, 0)
    mock_win.assert_not_called()
    mock_push.assert_not_called()
    mock_loss.assert_called_with(0)


@patch("milestone_2.End_Of_Game.win")
@patch("milestone_2.End_Of_Game.push")
@patch("milestone_2.End_Of_Game.loss")
@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: True,
)
def test_will_not_end_the_game_if_either_player_can_make_actions(
    mock_win, mock_push, mock_loss, player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when a player or the dealer can take an action, no method will be called.
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    handle_end_of_game(player_stub, dealer_stub, 0)
    mock_win.assert_not_called()
    mock_push.assert_not_called()
    mock_loss.assert_not_called()


@patch("builtins.print")
def test_on_win_displays_appropriate_message(mock_print, player_stub: Player) -> None:
    """
    Tests that when the player wins, an appropriate message is shown
    Args:
        player_stub: Stub of Player
    """
    initial_bets = [0, 20, 500]
    for initial_bet in initial_bets:
        win(player_stub, initial_bet)
        mock_print.assert_any_call("Congratulations! You won")
        mock_print.assert_any_call(
            f"Initial bet: {initial_bet}, Winnings: {initial_bet}"
        )
        mock_print.assert_any_call()


@patch("builtins.print")
def test_on_push_displays_appropriate_message(mock_print, player_stub: Player) -> None:
    """
    Tests that when the player draws with the dealer, an appropriate message is shown
    Args:
        player_stub: Stub of Player
    """
    initial_bets = [0, 20, 500]
    for initial_bet in initial_bets:
        push(player_stub, initial_bet)
        mock_print.assert_any_call("You drew")
        mock_print.assert_any_call(f"Initial bet: {initial_bet}, Winnings: 0")
        mock_print.assert_any_call()


@patch("builtins.print")
def test_on_loss_displays_appropriate_message(mock_print) -> None:
    """
    Tests that when the player loses, an appropriate message is shown
    """
    initial_bets = [0, 20, 500]
    for initial_bet in initial_bets:
        loss(initial_bet)
        mock_print.assert_any_call("Unlucky! You Lost")
        mock_print.assert_any_call(f"Initial bet: {initial_bet}, Winnings: 0")
        mock_print.assert_any_call()


def test_on_win_wallet_is_updated_correctly(player_stub: Player_Stub):
    """
    Tests that when the player wins, they are given the correct amount of winnings
    Args:
        player_stub: Stub of Player
    """
    initial_bets = [0, 20, 500]
    for initial_bet in initial_bets:
        win(player_stub, initial_bet)
        assert player_stub.funds_added == initial_bet * 2
        player_stub.funds_added = 0


def test_on_push_wallet_is_updated_correctly(player_stub: Player_Stub):
    """
    Tests that when the player draws with the dealers, they are refunded
    Args:
        player_stub: Stub of Player
    """
    initial_bets = [0, 20, 500]
    for initial_bet in initial_bets:
        push(player_stub, initial_bet)
        assert player_stub.funds_added == initial_bet
        player_stub.funds_added = 0
