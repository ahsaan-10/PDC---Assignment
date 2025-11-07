# Chapter2_Threading/thread_utils.py
import threading
# Import PrimeAnalyzer from the Chapter 1 package
from Chapter1_Basics_OOP.analyzer import PrimeAnalyzer

class ThreadWorker(threading.Thread):
    """
    (Ch 2) Custom Thread class inheriting from threading.Thread.
    """
    # Renamed 'start' and 'end' parameters to 'start_idx' and 'end_idx'
    def __init__(self, name, start_idx, end_idx, shared_results, lock):
        threading.Thread.__init__(self)
        self.name = name
        # FIX: Changed self.start to self.start_idx to avoid overwriting the built-in start() method
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.shared_results = shared_results
        # (Ch 2) Lock for synchronization
        self.lock = lock
        self.analyzer = PrimeAnalyzer()

    def run(self):
        """(Ch 2) The execution logic of the thread (entry point when start() is called)."""
        
        # Updated to use the new variable names
        local_primes = self.analyzer.calculate_in_range(self.start_idx, self.end_idx)

        # (Ch 2) Acquire the Lock before accessing shared resources
        # This prevents race conditions when multiple threads update the list simultaneously.
        self.lock.acquire()
        try:
            self.shared_results.extend(local_primes)
        finally:
            # (Ch 2) Release the Lock (Crucial to do this in a finally block)
            self.lock.release()
