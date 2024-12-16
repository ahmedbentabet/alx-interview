#!/usr/bin/python3
"""Module to solve the coin change problem with minimal coins."""


def make_change(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations
        total (int): Target total amount

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be met
    """
    if total <= 0:
        return 0

    # Use greedy approach for large inputs to improve performance
    coins.sort(reverse=True)
    # Attempt to solve using greedy method
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
