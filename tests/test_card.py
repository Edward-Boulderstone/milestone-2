import pytest

from milestone_2.Card import Card


def test_card_equality():
    assert Card("Heart", 2) == Card("Heart", 2)
    assert Card("Spade", 1) == Card("Spade", 1)
    assert Card("Diamond", 13) == Card("Diamond", 13)
    assert Card("Club", 5) == Card("Club", 5)


def test_card_out_of_bounds_fails():
    with pytest.raises(AssertionError):
        Card("S", 2)

    with pytest.raises(AssertionError):
        Card("Hearts", 2)

    with pytest.raises(AssertionError):
        Card("Heart", -1)

    with pytest.raises(AssertionError):
        Card("Heart", 15)
