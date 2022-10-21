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
def ace_hand(ace: TestCard, ten: TestCard) -> Hand:
    return Hand(ace, ten)


@pytest.fixture
def sixteen_hand(six: TestCard, ten: TestCard) -> Hand:
    return Hand(six, ten)


def test_starting_hand_value(ace_hand: Hand, sixteen_hand: Hand) -> None:
    assert ace_hand.value() == 21
    assert sixteen_hand.value() == 16


def test_drawing_card_updates_value(
    ace_hand: Hand, sixteen_hand: Hand, ten: TestCard, six: TestCard
) -> None:
    assert ace_hand.draw(ten).value() == 21
    assert sixteen_hand.draw(six).value() == 22


def test_is_bust(
    ace_hand: Hand, sixteen_hand: Hand, ten: TestCard, six: TestCard
) -> None:
    assert not ace_hand.is_bust()
    assert not sixteen_hand.is_bust()
    assert not ace_hand.draw(ten).is_bust()
    assert sixteen_hand.draw(six).is_bust()
