class Wallet:
    def __init__(self, funds: int = 2000) -> None:
        self.funds = funds

    def total(self) -> int:
        return self.funds

    def add_funds(self, funds_to_add: int) -> None:
        """
        Adds funds to wallet
        Args:
            funds_to_add: funds to add to wallet
        """
        self.funds += funds_to_add

    def spend(self, funds_to_remove: int) -> None:
        """
        Removes money from a wallet, throws assertion error when not enough funds to remove
        Args:
            funds_to_remove: Funds to remove
        """
        assert self.funds >= funds_to_remove
        self.funds -= funds_to_remove
