import pytest

from milestone_2.Deck import Deck


@pytest.fixture
def deck_size() -> int:
    return 52


def test_deck_initializes_with_52_unique_cards() -> None:
    assert len(Deck()) == deck_size()
    assert len(set(Deck())) == deck_size()


def test_deck_removes_card_when_drawn() -> None:
    deck = Deck()
    current_deck_size = deck_size()
    cards_in_deck = []
    for card_index in range(deck_size()):
        cards_in_deck.append(deck.draw())
        current_deck_size -= 1
        assert len(deck) == current_deck_size
    assert len(set(cards_in_deck)) == 52
