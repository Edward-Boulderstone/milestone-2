from _pytest.fixtures import fixture

from milestone_2.Blackjack_Player import Blackjack_Player


@fixture
def player() -> Blackjack_Player:
    return Blackjack_Player()


@fixture
def bust_player() -> Blackjack_Player:
    bust_player = Blackjack_Player()
    try:
        for _ in range(6):
            bust_player.hit()
    except AssertionError:
        pass
    return bust_player


def test_is_bust(player: Blackjack_Player, bust_player: Blackjack_Player) -> None:
    """
    Tests that a player can be identified as bust
    Args:
        player: A player with a non-bust hand
        bust_player: A player with a bust hand
    """
    assert not player.is_bust()
    assert bust_player.is_bust()


def test_cant_make_actions_when_bust(bust_player: Blackjack_Player) -> None:
    """
    Tests that a bust player cannot hit
    Args:
        bust_player:  Player with a bust hand
    """
    initial_cards_in_hand = len(bust_player.hand.hand)
    bust_player.hit()
    assert initial_cards_in_hand == len(bust_player.hand.hand)


def test_can_hit(player: Blackjack_Player) -> None:
    """
    Tests that a player can add a card to their hand
    Args:
        player: Player with non-bust hand
    """
    initial_cards_in_hand = len(player.hand.hand)
    player.hit()
    assert initial_cards_in_hand + 1 == len(player.hand.hand)


def test_can_stand(player: Blackjack_Player) -> None:
    """
    Tests that a player can stand, and this prevents them from hitting
    Args:
        player:  Player with a non-bust hand
    """
    initial_cards_in_hand = len(player.hand.hand)
    player.stand()
    player.hit()
    assert initial_cards_in_hand == len(player.hand.hand)


def test_player_resets_hand(player: Blackjack_Player):
    """
    Tests that when the player has their hand reset, they get a new hand with 2 cards in it
    Args:
        player: A generic player
    """
    first_hand = player.hand
    player.reset_for_next_game()
    assert not first_hand == player.hand
    assert len(player.hand.hand) == 2


def test_player_initial_hand(player: Blackjack_Player):
    """
    Tests that when the player gets their initial hand it has two cards in it
    Args:
        player: A freshly initialised player
    """
    assert len(player.hand.hand) == 2
