#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of the prime number game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str or None: Name of the winner ("Maria" or "Ben"),
                    or None if there's a tie.
    """
    def sieve_of_eratosthenes(max_n):
        """Generate a list of prime counts up to max_n."""
        sieve = [True] * (max_n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_n + 1, i):
                    sieve[j] = False
        # Count primes up to each number
        prime_counts = [0] * (max_n + 1)
        count = 0
        for i in range(1, max_n + 1):
            if sieve[i]:
                count += 1
            prime_counts[i] = count
        return prime_counts

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_counts = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

