import pytest

from milestone_2.Hand import Hand


class TestCard:
    def __init__(self, value: int) -> None:
        self.value = value

    def get_card_value(self) -> int:
        return self.value


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
    return TestCard(6)


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
    assert blackjack_hand.value() == 21
    assert ace_hand.value() == 17


def test_standard_hand_value(sixteen_hand: Hand, seventeen_hand: Hand) -> None:
    assert sixteen_hand.value() == 16
    assert seventeen_hand.value() == 17


def test_drawing_card_updates_value(
    blackjack_hand: Hand, sixteen_hand: Hand, ten: TestCard, six: TestCard
) -> None:
    assert blackjack_hand.draw(ten).value() == 21
    assert sixteen_hand.draw(six).value() == 22


def test_is_bust(
    blackjack_hand: Hand, sixteen_hand: Hand, ten: TestCard, six: TestCard
) -> None:
    assert not blackjack_hand.is_bust()
    assert not sixteen_hand.is_bust()
    assert not blackjack_hand.draw(ten).is_bust()
    assert sixteen_hand.draw(six).is_bust()


def test_comparison_of_standard_hands() -> None:
    hand_15 = test_hand(6, 9)
    hand_5 = test_hand(2, 3)
    hand_21 = test_hand(4, 7, 10)

    assert hand_15 > hand_5
    assert hand_15 < hand_21
    assert hand_5 < hand_21


def test_comparison_of_equal_valued_hands() -> None:
    hand_15_lhs = test_hand(6, 9)
    hand_5_lhs = test_hand(2, 3)
    hand_21_lhs = test_hand(4, 7, 10)

    hand_15_rhs = test_hand(5, 10)
    hand_5_rhs = test_hand(4, 1)
    hand_21_rhs = test_hand(9, 7, 4)

    assert hand_15_lhs == hand_15_rhs
    assert hand_5_lhs == hand_5_rhs
    assert hand_21_lhs == hand_21_rhs


def test_comparison_of_black_and_21(blackjack_hand: Hand) -> None:
    hand_21 = test_hand(4, 7, 10)

    assert blackjack_hand > hand_21


def test_bust_hand_always_less_than_other_hands() -> None:
    burst_hand = test_hand(10, 3, 9)
    hand_15 = test_hand(6, 9)
    hand_4 = test_hand(2, 2)
    hand_21 = test_hand(4, 7, 10)

    assert burst_hand < hand_4
    assert burst_hand < hand_15
    assert burst_hand < hand_21


def test_bust_hand_always_equal_to_other_bust_hands() -> None:
    burst_hand_1 = test_hand(10, 3, 9)
    burst_hand_2 = test_hand(9, 9, 9)
    burst_hand_3 = test_hand(6, 9, 7)

    assert burst_hand_1 == burst_hand_2
    assert burst_hand_1 == burst_hand_3
    assert burst_hand_2 == burst_hand_3


def test_ace_in_hand_compare() -> None:
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
        assert ace_hand > hand_18
