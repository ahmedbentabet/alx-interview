#!/usr/bin/python3
"""Module to solve the coin change problem with minimal coins."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations
        total (int): Target total amount

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be met
    """
    # Handle edge cases
    if total <= 0:
        return 0

    # Initialize DP table with max value (unreachable)
    # We use total + 1 as an "impossible" marker
    dp = [total + 1] * (total + 1)

    # Base case: 0 coins needed to make 0
    dp[0] = 0

    # Build solution bottom-up
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result, or -1 if total cannot be made
    return dp[total] if dp[total] != total + 1 else -1
