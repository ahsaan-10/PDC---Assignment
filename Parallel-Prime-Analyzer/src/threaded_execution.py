# src/threaded_execution.py
import threading
import time
from analyzer import PrimeAnalyzer

MAX_NUM = 200000
NUM_WORKERS = 4 # Number of threads

# Shared resources (Chap 2)
# Threads share the same memory space, so this list is accessible by all.
threaded_results = []
# Lock definition (Chap 2) to prevent race conditions when updating the list.
threadLock = threading.Lock()

def worker(analyzer, start, end):
    """Function executed by each thread."""
    local_primes = analyzer.calculate_in_range(start, end)

    # Safely update the shared list using the lock (Chap 2)
    # Acquire the lock before modification
    threadLock.acquire()
    try:
        threaded_results.extend(local_primes)
    finally:
        # Release the lock after modification
        threadLock.release()

if __name__ == "__main__":
    print(f"--- Threaded Execution ---")
    print(f"Analyzing up to {MAX_NUM} with {NUM_WORKERS} threads...")
    analyzer = PrimeAnalyzer()
    threads = []
    chunk_size = MAX_NUM // NUM_WORKERS

    start_time = time.time()

    # Create and start threads (Chap 1 & 2)
    for i in range(NUM_WORKERS):
        # Calculate the range for the current thread
        start_idx = i * chunk_size
        # Ensure the last thread covers the remaining range up to MAX_NUM
        if i == NUM_WORKERS - 1:
            end_idx = MAX_NUM
        else:
            end_idx = (i + 1) * chunk_size

        # Handle the start index adjustment (avoid recalculating 0 if i=0)
        if start_idx == 0:
            start_idx = 1

        t = threading.Thread(target=worker, args=(analyzer, start_idx, end_idx))
        threads.append(t)
        t.start()

    # Wait for all threads to complete (Chap 2: Joining)
    for t in threads:
        t.join()

    end_time = time.time()

    print("-" * 30)
    # Note: Due to the Global Interpreter Lock (GIL), this might not be faster than serial for CPU-bound tasks.
    print(f"Threaded Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Total primes found: {len(threaded_results)}")
    print("-" * 30)
