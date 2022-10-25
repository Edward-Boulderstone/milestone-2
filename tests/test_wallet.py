import pytest

from milestone_2.Wallet import Wallet


@pytest.fixture
def new_wallet() -> Wallet:
    return Wallet()


@pytest.fixture
def empty_wallet() -> Wallet:
    return Wallet(0)


def test_wallet_initializes_with_2000_funds(new_wallet: Wallet) -> None:
    """
    Tests that a new wallet initializes with 2000 funds
    Args:
        new_wallet: A new wallet
    """
    assert new_wallet.total() == 2000


def test_wallet_can_add_and_subtract_funds(new_wallet: Wallet) -> None:
    """
    Tests that funds can be added to a wallet
    Args:
        new_wallet:  A new wallet
    """
    new_wallet_funds = new_wallet.total()
    new_wallet.add_funds(100)
    assert new_wallet.total() == new_wallet_funds + 100
    new_wallet.add_funds(300)
    assert new_wallet.total() == new_wallet_funds + 100 + 300


def test_wallet_can_subtract_funds(new_wallet: Wallet) -> None:
    """
    Tests that funds can be removed from a wallet
    Args:
        new_wallet:  A new wallet
    """
    new_wallet_funds = new_wallet.total()
    new_wallet.spend(200)
    assert new_wallet.total() == new_wallet_funds - 200
    new_wallet.spend(800)
    assert new_wallet.total() == new_wallet_funds - 200 - 800


def test_wallet_can_not_subtract_funds_from_empty_wallet(empty_wallet: Wallet) -> None:
    """
    Tests that an empty wallet cannot spend any funds
    Args:
        empty_wallet: An empty wallet
    """
    with pytest.raises(AssertionError):
        empty_wallet.spend(10)

    with pytest.raises(AssertionError):
        empty_wallet.spend(20)
