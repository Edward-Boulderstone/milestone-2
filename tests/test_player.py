from unittest.mock import MagicMock
from _pytest.monkeypatch import MonkeyPatch
from pytest import fixture

from milestone_2.Player import Player


@fixture
def player() -> Player:
    return Player()


@fixture
def bust_player() -> Player:
    bust_player = Player()
    try:
        for _ in range(6):
            bust_player.hit()
    except AssertionError:
        pass
    return bust_player


def mock_user_input(mocked_input: str) -> None:
    monkeypatch_session = MonkeyPatch()

    def mock_input(*args: tuple[str]) -> str:
        return mocked_input

    monkeypatch_session.setattr("builtins.input", mock_input)


def test_is_bust(player, bust_player: Player) -> None:
    """
    Tests that a player can be identified as bust
    Args:
        player: A player with a non-bust hand
        bust_player: A player with a bust hand
    """
    assert not player.is_bust()
    assert bust_player.is_bust()


def test_can_hit(player) -> None:
    """
    Tests that a player can add a card to their hand
    Args:
        player: Player with non-bust hand
    """
    initial_cards_in_hand = len(player.hand.hand)
    player.hit()
    assert initial_cards_in_hand + 1 == len(player.hand.hand)


def test_can_stand(player) -> None:
    """
    Tests that a player can stand, and this prevents them from hitting
    Args:
        player:  Player with a non-bust hand
    """
    initial_cards_in_hand = len(player.hand.hand)
    player.stand()
    player.hit()
    assert initial_cards_in_hand == len(player.hand.hand)


def test_cant_make_actions_when_bust(bust_player: Player) -> None:
    """
    Tests that a bust player cannot hit
    Args:
        bust_player:  Player with a bust hand
    """
    initial_cards_in_hand = len(bust_player.hand.hand)
    bust_player.hit()
    assert initial_cards_in_hand == len(bust_player.hand.hand)


def test_user_can_choose_to_hit_on_their_turn(
    player,
) -> None:
    """
    Tests that the user inputting Hit will call the hit method
    Args:
        player: A player with a non-bust hand
    """
    mock_user_input("Hit")
    player.hit = MagicMock()
    player.handle_turn()
    player.hit.assert_called_with()


def test_user_can_choose_to_legally_stand_on_their_turn(
    player,
) -> None:
    """
    Tests that the user inputting Stand will call the stand method
    Args:
        player: A player with a non-bust hand
    """
    mock_user_input("Stand")
    player.stand = MagicMock()
    player.handle_turn()
    player.stand.assert_called_with()


def test_player_resets_hand(player):
    """
    Tests that when the player has their hand reset, they get a new hand with 2 cards in it
    Args:
        player_with_starting_hand: A generic player
    """
    first_hand = player.hand
    player.reset_for_next_game()
    assert not first_hand == player.hand
    assert len(player.hand.hand) == 2


def test_player_initial_hand(player):
    """
    Tests that when the player gets their initial hand it has two cards in it
    Args:
        player_with_starting_hand: A freshly initialised player
    """
    assert len(player.hand.hand) == 2
