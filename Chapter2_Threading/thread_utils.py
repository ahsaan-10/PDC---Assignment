# Chapter2_Threading/thread_utils.py
import threading
# Import PrimeAnalyzer from the Chapter 1 package
from Chapter1_Basics_OOP.analyzer import PrimeAnalyzer

class ThreadWorker(threading.Thread):
    """
    (Ch 2) Custom Thread class inheriting from threading.Thread.
    """
    def __init__(self, name, start, end, shared_results, lock):
        threading.Thread.__init__(self)
        self.name = name
        self.start = start
        self.end = end
        self.shared_results = shared_results
        # (Ch 2) Lock for synchronization
        self.lock = lock
        self.analyzer = PrimeAnalyzer()

    def run(self):
        """(Ch 2) The execution logic of the thread (entry point when start() is called)."""
        
        local_primes = self.analyzer.calculate_in_range(self.start, self.end)

        # (Ch 2) Acquire the Lock before accessing shared resources
        # This prevents race conditions when multiple threads update the list simultaneously.
        self.lock.acquire()
        try:
            self.shared_results.extend(local_primes)
        finally:
            # (Ch 2) Release the Lock (Crucial to do this in a finally block)
            self.lock.release()
