from milestone_2.Blackjack_Player import Blackjack_Player
from milestone_2.Player import Player


def handle_end_of_game(
    player: Player, dealer: Blackjack_Player, bet_amount: int
) -> None:
    if player.can_perform_actions() or dealer.can_perform_actions():
        return
    if player.hand > dealer.hand:
        return win(player, bet_amount)
    if player.hand == dealer.hand:
        return push(player, bet_amount)
    return loss(bet_amount)


def win(user: Player, bet_amount: int) -> None:
    print("Congratulations! You won")
    print(f"Initial bet: {bet_amount}, Winnings: {bet_amount}")
    print()
    user.add_funds(bet_amount * 2)


def push(user: Player, bet_amount: int) -> None:
    print("You drew")
    print(f"Initial bet: {bet_amount}, Winnings: 0")
    print()
    user.add_funds(bet_amount)


def loss(bet_amount: int) -> None:
    print("Unlucky! You Lost")
    print(f"Initial bet: {bet_amount}, Winnings: 0")
    print()
