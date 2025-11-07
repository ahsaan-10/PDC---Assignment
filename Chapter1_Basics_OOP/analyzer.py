# Chapter1_Basics_OOP/analyzer.py

class PrimeAnalyzer:
    """
    (Ch 1) A class to analyze prime numbers. Demonstrates OOP.
    """
    def __init__(self):
        # (Ch 1) Initialize instance variables
        self.description = "Prime Number Calculator"

    def is_prime(self, n):
        """(Ch 1) Checks if a number n is prime using control flow (if/while)."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        # (Ch 1) Using a while loop for optimization (checking up to sqrt(n))
        i = 5
        while i * i <= n:
            # Check factors in the form 6k +/- 1
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_in_range(self, start, end):
        """(Ch 1) Calculates primes using a for loop."""
        primes = []
        for num in range(start, end):
            if self.is_prime(num):
                primes.append(num)
        
        # (Ch 1) Demonstrating File I/O - Logging the work done by this chunk
        # We append ('a') to the file so different threads/processes can write to it.
        try:
            # Note: File I/O here demonstrates the concept, but can slow down parallel execution.
            # In a real-world scenario, concurrent file writing requires careful synchronization.
            with open('calculation_log.txt', 'a') as f:
                f.write(f"Chunk analyzed: {start}-{end}. Primes found: {len(primes)}\n")
        except IOError as e:
            # Suppress errors during rapid parallel execution
            pass
            
        return primes
