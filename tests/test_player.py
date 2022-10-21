import pytest

from milestone_2.Player import Player


@pytest.fixture
def player_with_starting_hand() -> Player:
    player = Player()
    player.draw_starting_hand()
    return player


@pytest.fixture
def bust_player(player_with_starting_hand: Player) -> Player:
    player_with_starting_hand.draw_starting_hand()
    try:
        for _ in range(6):
            player_with_starting_hand.hit()
    except AssertionError:
        pass
    return player_with_starting_hand


def test_is_bust() -> None:
    assert False


def test_can_hit() -> None:
    assert False


def test_can_stand() -> None:
    assert False


def test_cant_make_actions_when_bust() -> None:
    assert False


def test_cant_bet_more_chips_than_own() -> None:
    assert False
