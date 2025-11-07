# src/analyzer.py

class PrimeAnalyzer:
    """
    A class to analyze prime numbers within a given range.
    Incorporates OOP principles (Chap 1).
    """
    def __init__(self):
        # Initialize instance variables
        self.description = "Prime Number Calculator"

    def is_prime(self, n):
        """Checks if a number n is prime using control flow (Chap 1)."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        # Check if divisible by 2 or 3
        if n % 2 == 0 or n % 3 == 0:
            return False

        # Using a while loop (Chap 1) to check for factors up to sqrt(n)
        # Optimization: We only check factors in the form 6k +/- 1
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_in_range(self, start, end):
        """Calculates all primes between start (inclusive) and end (exclusive)."""
        primes = []
        # Using a for loop (Chap 1)
        for num in range(start, end):
            if self.is_prime(num):
                primes.append(num)
        return primes
