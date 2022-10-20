from milestone_2 import Dealer


def test_average_card_delt():
    dealer = Dealer()
    cards_to_deal = 5200
    cards_delt = [dealer.deal_card() for _ in range(cards_to_deal)]
    assert len(cards_delt) == 5200
    assert len(set(cards_delt)) == 52


def test_starting_hand_deal():
    dealer = Dealer()
    starting_hand = dealer.deal_starting_hand()
    assert len(starting_hand) == 2
