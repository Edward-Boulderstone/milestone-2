import pytest

from milestone_2.Card import Card
from milestone_2.Hand import Hand


class TestCard(Card):
    def __init__(self, value: int) -> None:
        super().__init__("Heart", value)
        self.value = value

    def get_value(self) -> int:
        return self.value

    def __str__(self):
        return str(self.value)


@pytest.fixture
def ace() -> TestCard:
    return TestCard(11)


@pytest.fixture
def ten() -> TestCard:
    return TestCard(10)


@pytest.fixture
def six() -> TestCard:
    return TestCard(6)


@pytest.fixture
def seven() -> TestCard:
    return TestCard(7)


@pytest.fixture
def blackjack_hand(ace: TestCard, ten: TestCard) -> Hand:
    return Hand(ace, ten)


@pytest.fixture
def ace_hand(ace: TestCard, six: TestCard) -> Hand:
    return Hand(ace, six)


@pytest.fixture
def sixteen_hand(six: TestCard, ten: TestCard) -> Hand:
    return Hand(six, ten)


@pytest.fixture
def seventeen_hand(seven: TestCard, ten: TestCard) -> Hand:
    return Hand(seven, ten)


def test_hand(*card_values: int) -> Hand:
    test_cards = [TestCard(card_value) for card_value in card_values]
    return Hand(*test_cards)


def test_ace_can_be_high_in_hand_value(blackjack_hand: Hand, ace_hand: Hand) -> None:
    """
    Tests if the hand can treat ace as 11 in calculating its value
    Args:
        blackjack_hand: A blackjack hand with an ace and a ten
        ace_hand: A hand with an ace, and a 6
    """
    assert blackjack_hand.value() == 21
    assert ace_hand.value() == 17


def test_standard_hand_value(sixteen_hand: Hand, seventeen_hand: Hand) -> None:
    """
    Tests if the hand can calculate the value of a standard blackjack hand
    Args:
        sixteen_hand: hand with a six and a ten
        seventeen_hand: hand with a seven and a ten

    Returns:

    """
    assert sixteen_hand.value() == 16
    assert seventeen_hand.value() == 17


def test_drawing_card_updates_value(
    blackjack_hand: Hand, sixteen_hand: Hand, ten: TestCard, six: TestCard
) -> None:
    """
    Tests that a Hand can draw a card, and then update the value of the hand correctly.
    Args:
        blackjack_hand: A blackjack hand with an ace and a ten
        sixteen_hand: A hand with a six and a ten
        ten: A card of value 10
        six: A card of value 6
    """
    assert blackjack_hand.draw(ten).value() == 21
    assert sixteen_hand.draw(six).value() == 22


def test_is_bust(
    blackjack_hand: Hand, sixteen_hand: Hand, ten: TestCard, six: TestCard
) -> None:
    """
    Tests if a hand can recognise that it is bust
    Args:
        blackjack_hand: A blackjack hand with an ace and a ten
        sixteen_hand: A hand with a six and a ten
        ten: A card of value 10
        six: A card of value 6
    """
    assert not blackjack_hand.is_bust()
    assert not sixteen_hand.is_bust()
    assert not blackjack_hand.draw(ten).is_bust()
    assert sixteen_hand.draw(six).is_bust()


def test_comparison_of_standard_hands() -> None:
    """
    Tests that two standard hands can be compared using greater than and the less than operators
    """
    hand_15 = test_hand(6, 9)
    hand_5 = test_hand(2, 3)
    hand_21 = test_hand(4, 7, 10)

    assert hand_15 > hand_5
    assert hand_15 < hand_21
    assert hand_5 < hand_21


def test_comparison_of_equal_valued_hands() -> None:
    """
    Tests that two standard hands can be compared using equals operator and the result is based on blackjack value
    """
    hand_15_lhs = test_hand(6, 9)
    hand_5_lhs = test_hand(2, 3)
    hand_21_lhs = test_hand(4, 7, 10)

    hand_15_rhs = test_hand(5, 10)
    hand_5_rhs = test_hand(4, 1)
    hand_21_rhs = test_hand(9, 7, 5)

    assert hand_15_lhs == hand_15_rhs
    assert hand_5_lhs == hand_5_rhs
    assert hand_21_lhs == hand_21_rhs

    assert not hand_15_lhs == hand_5_rhs
    assert not hand_5_lhs == hand_21_rhs
    assert not hand_15_lhs == hand_21_rhs


def test_comparison_of_blackjack_and_21(blackjack_hand: Hand) -> None:
    """
    Tests that a hand with 21 is less than the value of a blackjack hand
    Args:
        blackjack_hand: A hand with an ace and ten, an unbeatable hand
    """
    hand_21 = test_hand(4, 7, 10)
    assert blackjack_hand > hand_21


def test_bust_hand_always_less_than_other_hands() -> None:
    """
    Tests that a burst hand always has a lesser blackjack value than every other hand
    """
    burst_hand = test_hand(10, 3, 9)
    hand_15 = test_hand(6, 9)
    hand_4 = test_hand(2, 2)
    hand_21 = test_hand(4, 7, 10)

    assert burst_hand < hand_4
    assert burst_hand < hand_15
    assert hand_21 > burst_hand


def test_bust_hand_always_equal_to_other_bust_hands() -> None:
    """
    Tests that two burst hands always have the same blackjack value
    """
    burst_hand_1 = test_hand(10, 3, 9)
    burst_hand_2 = test_hand(9, 9, 9)
    burst_hand_3 = test_hand(6, 9, 7)

    assert burst_hand_1 == burst_hand_2
    assert burst_hand_1 == burst_hand_3
    assert burst_hand_2 == burst_hand_3


def test_ace_in_hand_compare() -> None:
    """
    Tests ace high and ace low are both handled the same if their blackjack value is equal
    """
    hand_17_with_high_ace = test_hand(11, 6)
    hand_17_with_low_ace = test_hand(11, 6, 10)
    hand_17 = test_hand(10, 7)
    hand_16 = test_hand(10, 6)
    hand_18 = test_hand(10, 8)
    ace_hands = [hand_17_with_low_ace, hand_17_with_high_ace]
    assert ace_hands[0] == ace_hands[1]
    for ace_hand in ace_hands:
        assert ace_hand > hand_16
        assert ace_hand == hand_17
        assert ace_hand < hand_18


def test_hand_displays_cards(
    blackjack_hand: Hand, ace_hand: Hand, sixteen_hand: Hand
) -> None:
    """
    Tests that the hand displays its cards it correctly
    """
    assert blackjack_hand.output() == "Hand = {11, 10}, Value = Blackjack"
    assert ace_hand.output() == "Hand = {11, 6}, Value = 17"
    assert sixteen_hand.output() == "Hand = {6, 10}, Value = 16"
    three_card_hand = test_hand(4, 7, 10)
    assert three_card_hand.output() == "Hand = {4, 7, 10}, Value = 21"


def test_hand_displays_first_card_when_hidden(
    blackjack_hand: Hand, ace_hand: Hand, sixteen_hand: Hand
) -> None:
    assert blackjack_hand.output(True) == "Hand = {11, *}"
    assert ace_hand.output(True) == "Hand = {11, *}"
    assert sixteen_hand.output(True) == "Hand = {6, *}"
    three_card_hand = test_hand(4, 7, 10)
    assert three_card_hand.output(True) == "Hand = {4, *, *}"
