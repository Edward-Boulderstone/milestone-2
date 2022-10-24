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


def test_is_bust(player_with_starting_hand: Player, bust_player: Player) -> None:
    assert not player_with_starting_hand.is_bust()
    assert bust_player.is_bust()


def test_can_hit(player_with_starting_hand: Player) -> None:
    inital_cards_in_hand = len(player_with_starting_hand.hand)
    player_with_starting_hand.hit()
    assert inital_cards_in_hand == 1 + len(player_with_starting_hand.hand)


def test_can_stand(player_with_starting_hand: Player) -> None:
    inital_cards_in_hand = len(player_with_starting_hand.hand)
    player_with_starting_hand.stand()
    player_with_starting_hand.hit()
    assert inital_cards_in_hand == len(player_with_starting_hand.hand)


def test_cant_make_actions_when_bust(bust_player: Player) -> None:
    inital_cards_in_hand = len(bust_player.hand)
    bust_player.hit()
    assert inital_cards_in_hand == len(bust_player.hand)


def test_cant_bet_more_chips_than_own() -> None:
    assert False
