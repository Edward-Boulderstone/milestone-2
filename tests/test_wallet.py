import pytest

from milestone_2.Wallet import Wallet


@pytest.fixture
def new_wallet() -> Wallet:
    return Wallet()


def empty_wallet() -> Wallet:
    return Wallet(0)


def test_wallet_initializes_with_2000_coins(new_wallet: Wallet) -> None:
    assert new_wallet.total() == 2000


def test_wallet_can_add_and_subtract_funds(
    new_wallet: Wallet, empty_wallet: Wallet
) -> None:
    assert new_wallet.total() == 2000
    new_wallet.spend(200)
    assert new_wallet.total() == 1800
    new_wallet.add_funds(600)
    assert new_wallet.total() == 2400
    with pytest.raises(AssertionError):
        empty_wallet.spend(10)
