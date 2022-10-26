from unittest.mock import patch, MagicMock
from _pytest.fixtures import fixture
from milestone_2.Dealer_AI import Dealer_AI
from milestone_2.Hand import Hand


class HandStub(Hand):
    def __init__(self, value: int = 0, output: str = "") -> None:
        super().__init__()
        self.hand_value = value
        self.output_ = output

    def value(self) -> int:
        return self.hand_value

    def output(self, hidden: bool = False) -> str:
        if hidden:
            return self.output_
        return f"{self.output_} but hidden"


@fixture
def dealer_ai() -> Dealer_AI:
    return Dealer_AI()


@fixture
def two_hand() -> HandStub:
    return HandStub(2)


@fixture
def fifteen_hand() -> HandStub:
    return HandStub(15)


@fixture
def sixteen_hand() -> HandStub:
    return HandStub(16)


@fixture
def seventeen_hand() -> HandStub:
    return HandStub(17)


@fixture
def eighteen_hand() -> HandStub:
    return HandStub(18)


@fixture
def nineteen_hand() -> HandStub:
    return HandStub(19)


def test_dealer_needs_to_hit_when_below_17(
    dealer_ai: Dealer_AI, two_hand: Hand, sixteen_hand: Hand, fifteen_hand: Hand
) -> None:
    """
    Test that the dealer AI will want to hit when its hand value is below 17
    Args:
        dealer_ai:  A dealer AI
    """
    dealer_ai.set_target_hand(two_hand)
    dealer_ai.hand = sixteen_hand
    assert dealer_ai.need_to_hit()
    dealer_ai.set_target_hand(fifteen_hand)
    dealer_ai.hand = fifteen_hand
    assert dealer_ai.need_to_hit()


def test_dealer_needs_to_hit_when_below_player(
    dealer_ai: Dealer_AI, seventeen_hand: Hand, eighteen_hand: Hand, nineteen_hand: Hand
) -> None:
    """
    Test that the dealer AI will want to hit when its hand value its target
    Args:
        dealer_ai:  A dealer AI
    """
    dealer_ai.set_target_hand(eighteen_hand)
    dealer_ai.hand = seventeen_hand
    assert dealer_ai.need_to_hit()

    dealer_ai.set_target_hand(nineteen_hand)
    dealer_ai.hand = eighteen_hand
    assert dealer_ai.need_to_hit()


def test_always_stands_above_17_and_player(
    dealer_ai: Dealer_AI, seventeen_hand: Hand, eighteen_hand: Hand, nineteen_hand: Hand
) -> None:
    """
    Test that the dealer AI will always stand when above 17 and the player
    Args:
        dealer_ai:  A dealer AI
    """
    dealer_ai.set_target_hand(seventeen_hand)
    dealer_ai.hand = eighteen_hand
    assert not dealer_ai.need_to_hit()

    dealer_ai.set_target_hand(eighteen_hand)
    dealer_ai.hand = nineteen_hand
    assert not dealer_ai.need_to_hit()


def test_cannot_perform_actions_when_hand_to_beat_is_not_set(
    dealer_ai: Dealer_AI, seventeen_hand: Hand
) -> None:
    """
    Tests that the dealer AI cannot make actions without a player hand to try to beat
    Args:
        dealer_ai:  A dealer AI
    """
    assert not dealer_ai.can_perform_actions()
    dealer_ai.set_target_hand(seventeen_hand)
    assert dealer_ai.can_perform_actions()


@patch("milestone_2.Dealer_AI.Dealer_AI.need_to_hit", lambda *args: True)
@patch("milestone_2.Dealer_AI.Dealer_AI.can_perform_actions", lambda *args: True)
def test_when_dealer_needs_hit_they_hit(dealer_ai: Dealer_AI) -> None:
    """
    Tests that when the need_to_hit method returns true and handle_turn is called, the Dealer_AI will hit
    Args:
        dealer_ai:  A dealer AI
    """
    dealer_ai.hit = MagicMock()
    dealer_ai.stand = MagicMock()
    dealer_ai.handle_turn()
    dealer_ai.hit.assert_called_with()
    dealer_ai.stand.assert_not_called()


@patch("milestone_2.Dealer_AI.Dealer_AI.need_to_hit", lambda *args: False)
@patch("milestone_2.Dealer_AI.Dealer_AI.can_perform_actions", lambda *args: True)
def test_when_dealer_does_not_need_to_hit_they_stand(dealer_ai: Dealer_AI) -> None:
    """
    Tests that when the need_to_hit method returns false and handle_turn is called, the Dealer_AI will stand
    Args:
        dealer_ai:  A dealer AI
    """
    dealer_ai.hit = MagicMock()
    dealer_ai.stand = MagicMock()
    dealer_ai.handle_turn()
    dealer_ai.stand.assert_called_with()
    dealer_ai.hit.assert_not_called()


def test_dealer_hand_displays_hand_hidden(dealer_ai: Dealer_AI) -> None:
    """
    Tests that the dealer's hand can be displayed with a single card, such as when the user is taking actions
    Args:
        dealer_ai:  A dealer AI
    """
    dealer_ai.hand = HandStub(output="Output")
    assert dealer_ai.display_hand_hidden() == "Output but hidden"
    dealer_ai.hand = HandStub(output="Test")
    assert dealer_ai.display_hand_hidden() == "Test but hidden"
