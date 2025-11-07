# src/multiprocess_execution.py
import multiprocessing
import time
from analyzer import PrimeAnalyzer

MAX_NUM = 200000
# Use the number of available CPU cores
NUM_WORKERS = multiprocessing.cpu_count()

# Helper function for Pool.map (must be top-level for multiprocessing to pickle it)
def process_worker(args):
    """Function executed by each process."""
    start_idx, end_idx = args
    # Create analyzer instance within the new process memory space
    analyzer = PrimeAnalyzer()
    return analyzer.calculate_in_range(start_idx, end_idx)

if __name__ == "__main__":
    # Crucial protection for multiprocessing
    multiprocessing.freeze_support()

    print(f"--- Multiprocessing Execution ---")
    print(f"Analyzing up to {MAX_NUM} with {NUM_WORKERS} processes...")
    chunk_size = MAX_NUM // NUM_WORKERS
    ranges = []

    # Prepare the arguments (tuples of start/end) for the map function
    for i in range(NUM_WORKERS):
        start_idx = i * chunk_size
        # Ensure the last process covers the remaining range
        if i == NUM_WORKERS - 1:
            end_idx = MAX_NUM
        else:
            end_idx = (i + 1) * chunk_size

        # Handle the start index adjustment
        if start_idx == 0:
            start_idx = 1
            
        ranges.append((start_idx, end_idx))

    start_time = time.time()

    # Using a Process Pool (Chap 3)
    # This bypasses the GIL and uses true parallelism.
    # Using 'with' ensures the pool is closed automatically
    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        # Map the worker function to the input ranges (Chap 3)
        # The pool handles distribution and collection of results.
        pool_outputs = pool.map(process_worker, ranges)

    end_time = time.time()

    # Combine results from the pool outputs
    # pool_outputs is a list of lists (one list from each process), so we flatten it
    mp_results = [item for sublist in pool_outputs for item in sublist]

    print("-" * 30)
    print(f"Multiprocessing Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Total primes found: {len(mp_results)}")
    print("-" * 30)
