from unittest.mock import patch, MagicMock
from _pytest.fixtures import fixture

from milestone_2 import End_Of_Game
from milestone_2.Blackjack_Player import Blackjack_Player
from milestone_2.End_Of_Game import handle_end_of_game
from milestone_2.Player import Player
from milestone_2.Wallet import Wallet


class Player_Stub(Player):
    def __init__(self):
        super().__init__()


@fixture
def player_stub() -> Player:
    return Player_Stub()


@fixture
def dealer_stub() -> Blackjack_Player:
    return Blackjack_Player()


@fixture
def wallet() -> Wallet:
    return Wallet()


def test_end_game_handling() -> None:
    assert False


@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: False,
)
@patch("milestone_2.Hand.Hand.__gt__", lambda *args: True)
@patch("milestone_2.Hand.Hand.__eq__", lambda *args: False)
def test_correct_identification_of_player_victory(
    player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when the user's hand is worth more than the dealer's and neither can take any actions,
    the win method will be called
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    End_Of_Game.win = MagicMock()
    End_Of_Game.push = MagicMock()
    End_Of_Game.loss = MagicMock()
    handle_end_of_game(player_stub, dealer_stub, 0)
    End_Of_Game.win.assert_called_with(player_stub, 0)
    End_Of_Game.push.assert_not_called()
    End_Of_Game.loss.assert_not_called()


@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: False,
)
@patch("milestone_2.Hand.Hand.__gt__", lambda *args: False)
@patch("milestone_2.Hand.Hand.__eq__", lambda *args: True)
def test_correct_identification_of_push(
    player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when the user's hand is worth the same as the dealer's and neither can take any actions,
    the push method will be called
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    End_Of_Game.win = MagicMock()
    End_Of_Game.push = MagicMock()
    End_Of_Game.loss = MagicMock()
    handle_end_of_game(player_stub, dealer_stub, 0)
    End_Of_Game.win.assert_not_called()
    End_Of_Game.push.assert_called_with(player_stub, 0)
    End_Of_Game.loss.assert_not_called()


@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: False,
)
@patch("milestone_2.Hand.Hand.__gt__", lambda *args: False)
@patch("milestone_2.Hand.Hand.__eq__", lambda *args: False)
def test_correct_identification_of_player_loss(
    player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when the dealer's hand is worth more than the user's and neither can take any actions,
    the loss method will be called
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    End_Of_Game.win = MagicMock()
    End_Of_Game.push = MagicMock()
    End_Of_Game.loss = MagicMock()
    handle_end_of_game(player_stub, dealer_stub, 0)
    End_Of_Game.win.assert_not_called()
    End_Of_Game.push.assert_not_called()
    End_Of_Game.loss.assert_called_with()


@patch(
    "milestone_2.Blackjack_Player.Blackjack_Player.can_perform_actions",
    lambda *args: False,
)
def test_will_not_end_the_game_if_either_player_can_make_actions(
    player_stub: Player, dealer_stub: Blackjack_Player
) -> None:
    """
    Tests that when a player or the dealer can take an action, no method will be called.
    Args:
        player_stub: Stub of Player
        dealer_stub: Stub of Dealer
    """
    End_Of_Game.win = MagicMock()
    End_Of_Game.push = MagicMock()
    End_Of_Game.loss = MagicMock()
    handle_end_of_game(player_stub, dealer_stub, 0)
    End_Of_Game.win.assert_not_called()
    End_Of_Game.push.assert_not_called()
    End_Of_Game.loss.assert_not_called()


def test_on_win_displays_appropriate_message(wallet: Wallet):
    """
    Tests that when the player wins, an appropriate message is shown
    Args:
        wallet: a wallet
    """
    assert False


def test_on_push_displays_appropriate_message(wallet: Wallet):
    """
    Tests that when the player draws with the dealer, an appropriate message is shown
    Args:
        wallet: a wallet
    """
    assert False


def test_on_loss_displays_appropriate_message():
    """
    Tests that when the player loses, an appropriate message is shown
    """
    assert False


def test_on_win_wallet_is_updated_correctly(wallet: Wallet):
    """
    Tests that when the player wins, they are given the correct amount of winnings
    Args:
        wallet: a wallet
    """
    assert False


def test_on_push_wallet_is_updated_correctly(wallet: Wallet):
    """
    Tests that when the player draws with the dealers, they are refunded
    Args:
        wallet: a wallet
    """
    assert False
