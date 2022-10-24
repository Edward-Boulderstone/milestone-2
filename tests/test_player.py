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
    assert not player_with_starting_hand.is_bust()
    assert bust_player.is_bust()


def test_can_hit(player_with_starting_hand: Player) -> None:
    initial_cards_in_hand = len(player_with_starting_hand.hand)
    player_with_starting_hand.hit()
    assert initial_cards_in_hand == 1 + len(player_with_starting_hand.hand)


def test_can_stand(player_with_starting_hand: Player) -> None:
    initial_cards_in_hand = len(player_with_starting_hand.hand)
    player_with_starting_hand.stand()
    player_with_starting_hand.hit()
    assert initial_cards_in_hand == len(player_with_starting_hand.hand)


def test_cant_make_actions_when_bust(bust_player: Player) -> None:
    initial_cards_in_hand = len(bust_player.hand)
    bust_player.hit()
    assert initial_cards_in_hand == len(bust_player.hand)


def test_user_can_choose_to_legally_hit_on_their_turn(
    player_with_starting_hand: Player, bust_player: Player
) -> None:
    mock_user_input("Hit")
    player_with_starting_hand.hit = MagicMock()
    player_with_starting_hand.handle_turn()
    player_with_starting_hand.hit.assert_called_with()

    bust_player.hit = MagicMock()
    bust_player.handle_turn()
    bust_player.hit.assert_not_called()


def test_user_can_choose_to_legally_stand_on_their_turn(
    player_with_starting_hand: Player, bust_player: Player
) -> None:
    mock_user_input("Stand")
    player_with_starting_hand.stand = MagicMock()
    player_with_starting_hand.handle_turn()
    player_with_starting_hand.stand.assert_called_with()

    bust_player.stand = MagicMock()
    bust_player.handle_turn()
    bust_player.stand.assert_not_called()
