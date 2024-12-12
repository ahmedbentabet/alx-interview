#!/usr/bin/python3
"""
Module to solve the Prime Game problem.

This module determines the winner of a game where players take turns
removing prime numbers and their multiples from a set of consecutive integers.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of game rounds
        nums (list): List of n values for each round

    Returns:
        str or None: Name of the player who won the most rounds
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

    def play_game(n):
        """
        Simulate a single round of the prime game.

        Args:
            n (int): Upper limit of the consecutive integers set

        Returns:
            str: Name of the winner ('Maria' or 'Ben')
        """
        # If n is too small, Ben wins immediately
        if n < 2:
            return 'Ben'

        # Track available numbers
        available = [True] * (n + 1)
        available[0] = available[1] = False

        current_player = 'Maria'
        while True:
            # Find the next prime number
            prime_found = False
            for prime in range(2, n + 1):
                if available[prime] and is_prime(prime):
                    prime_found = True
                    # Remove prime and its multiples
                    available[prime] = False
                    for multiple in range(prime, n + 1, prime):
                        available[multiple] = False
                    break

            # If no prime found, current player loses
            if not prime_found:
                return 'Ben' if current_player == 'Maria' else 'Maria'

            # Switch players
            current_player = 'Ben' if current_player == 'Maria' else 'Maria'

    # Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
