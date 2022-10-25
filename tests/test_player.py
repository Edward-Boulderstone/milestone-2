from unittest.mock import MagicMock
from _pytest.monkeypatch import MonkeyPatch
from pytest import fixture

from milestone_2.Player import Player


@fixture
def player_with_starting_hand() -> Player:
    player = Player()
    player.draw_starting_hand()
    return player


@fixture
def bust_player(player_with_starting_hand: Player) -> Player:
    player_with_starting_hand.draw_starting_hand()
    try:
        for _ in range(6):
            player_with_starting_hand.hit()
    except AssertionError:
        pass
    return player_with_starting_hand


@fixture
def mock_user_input(mocked_input: str) -> None:
    monkeypatch_session = MonkeyPatch()

    def mock_input(*args: tuple[str]) -> str:
        return mocked_input

    monkeypatch_session.setattr("builtins.input", mock_input)


def test_is_bust(player_with_starting_hand: Player, bust_player: Player) -> None:
    """
    Tests that a player can be identified as bust
    Args:
        player_with_starting_hand: A player with a non-bust hand
        bust_player: A player with a bust hand
    """
    assert not player_with_starting_hand.is_bust()
    assert bust_player.is_bust()


def test_can_hit(player_with_starting_hand: Player) -> None:
    """
    Tests that a player can add a card to their hand
    Args:
        player_with_starting_hand: Player with non-bust hand
    """
    initial_cards_in_hand = len(player_with_starting_hand.hand)
    player_with_starting_hand.hit()
    assert initial_cards_in_hand == 1 + len(player_with_starting_hand.hand)


def test_can_stand(player_with_starting_hand: Player) -> None:
    """
    Tests that a player can stand, and this prevents them from hitting
    Args:
        player_with_starting_hand:  Player with a non-bust hand
    """
    initial_cards_in_hand = len(player_with_starting_hand.hand)
    player_with_starting_hand.stand()
    player_with_starting_hand.hit()
    assert initial_cards_in_hand == len(player_with_starting_hand.hand)


def test_cant_make_actions_when_bust(bust_player: Player) -> None:
    """
    Tests that a bust player cannot hit
    Args:
        bust_player:  Player with a bust hand
    """
    initial_cards_in_hand = len(bust_player.hand)
    bust_player.hit()
    assert initial_cards_in_hand == len(bust_player.hand)


def test_user_can_choose_to_hit_on_their_turn(
    player_with_starting_hand: Player,
) -> None:
    """
    Tests that the user inputting Hit will call the hit method
    Args:
        player_with_starting_hand: A player with a non-bust hand
    """
    mock_user_input("Hit")
    player_with_starting_hand.hit = MagicMock()
    player_with_starting_hand.handle_turn()
    player_with_starting_hand.hit.assert_called_with()


def test_user_can_choose_to_legally_stand_on_their_turn(
    player_with_starting_hand: Player,
) -> None:
    """
    Tests that the user inputting Stand will call the stand method
    Args:
        player_with_starting_hand: A player with a non-bust hand
    """
    mock_user_input("Stand")
    player_with_starting_hand.stand = MagicMock()
    player_with_starting_hand.handle_turn()
    player_with_starting_hand.stand.assert_called_with()
