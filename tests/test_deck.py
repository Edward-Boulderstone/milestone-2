import pytest

from milestone_2.Deck import Deck


@pytest.fixture
def deck_size() -> int:
    return 52


def test_deck_initializes_with_52_unique_cards(deck_size: int) -> None:
    """
    Tests that the deck initializes with 52 cards unique cards=
    Args:
        deck_size: Expected deck size
    """
    assert len(Deck().deck) == deck_size
    assert len(set(Deck().deck)) == deck_size


def test_deck_removes_card_when_drawn(deck_size: int) -> None:
    """
    Tests that the deck removes cards when they are drawn from it
    Args:
        deck_size: Expected deck size
    """
    deck = Deck()
    current_deck_size = deck_size
    cards_in_deck = []
    for card_index in range(deck_size):
        cards_in_deck.append(deck.draw())
        current_deck_size -= 1
        assert len(deck.deck) == current_deck_size
    assert len(set(cards_in_deck)) == 52


def test_deck_throws_assertion_error_when_no_cards(deck_size: int) -> None:
    """
    Tests that the deck throws an error when you try to draw from it when it has no cards
    Args:
        deck_size: Expected deck size
    """
    deck = Deck()
    for _ in range(deck_size):
        deck.draw()
    with pytest.raises(AssertionError):
        deck.draw()
