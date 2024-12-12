#!/usr/bin/python3
"""
Module to solve the Prime Game problem.
"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(n):
    """
    Count the number of prime numbers up to n.

    Args:
        n (int): Upper limit of the range

    Returns:
        int: Count of prime numbers
    """
    primes = 0
    for i in range(2, n + 1):
        if is_prime(i):
            primes += 1
    return primes

def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of game rounds
        nums (list): List of n values for each round

    Returns:
        str or None: Name of the player who won the most rounds
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
