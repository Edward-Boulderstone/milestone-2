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


def test_user_can_choose_to_hit_on_their_turn(
    player: Player,
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
    player: Player,
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


def test_user_can_track_funds(player: Player) -> None:
    player.wallet.total = 200
    assert player.get_funds() == 200

    player.wallet.total = 20
    assert player.get_funds() == 20

    player.wallet.total = 5
    assert player.get_funds() == 5


def test_user_can_get_rewarded_with_funds() -> None:
    assert False


def test_user_can_bet_funds() -> None:
    assert False
