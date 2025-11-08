# main_comparison.py
import time
import threading
import multiprocessing
import os

# Import utilities from the chapter packages
# Added basic error handling for imports
try:
    from Chapter1_Basics_OOP.analyzer import PrimeAnalyzer
    # Ensure you are using the corrected version of thread_utils.py (using start_idx, end_idx)
    from Chapter2_Threading.thread_utils import ThreadWorker
    from Chapter3_Multiprocessing.process_utils import process_task
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please ensure you are running this script from the root directory of the project,")
    print("and that empty '__init__.py' files exist in each Chapter folder.")
    exit(1)


# Configuration
MAX_NUM = 200000 # The total range to analyze (CPU intensive task)

def prepare_environment():
    """Clears the log file before starting the tests."""
    if os.path.exists('calculation_log.txt'):
        os.remove('calculation_log.txt')
    # Create an empty log file
    open('calculation_log.txt', 'w').close()

def calculate_ranges(num_workers):
    """Helper to divide the MAX_NUM into chunks for workers."""
    chunk_size = MAX_NUM // num_workers
    ranges = []
    for i in range(num_workers):
        start_idx = i * chunk_size
        # Ensure the last worker covers the remaining range
        if i == num_workers - 1:
            end_idx = MAX_NUM
        else:
            end_idx = (i + 1) * chunk_size
        # Start checking from 1 instead of 0
        if start_idx == 0:
            start_idx = 1
        ranges.append((start_idx, end_idx))
    return ranges

# --- Serial Execution (Baseline - Ch 1) ---
def run_serial():
    print("\n--- Running Serial Execution ---")
    analyzer = PrimeAnalyzer()
    start_time = time.time()
    results = analyzer.calculate_in_range(1, MAX_NUM)
    end_time = time.time()
    print(f"Serial processing complete. Primes found: {len(results)}")
    print(f"Serial time = {end_time - start_time:.4f}")

# --- Multithreading Execution (Chapter 2) ---
def run_multithreading(num_threads):
    print(f"\n--- Running Multithreading ({num_threads} threads) ---")
    shared_results = []
    # (Ch 2) Initialize the lock
    thread_lock = threading.Lock()
    threads = []
    ranges = calculate_ranges(num_threads)

    start_time = time.time()

    # (Ch 2) Create and start threads using the custom class
    # We pass the start_idx and end_idx which the ThreadWorker expects
    for i, (start_idx, end_idx) in enumerate(ranges):
        t = ThreadWorker(f"T{i+1}", start_idx, end_idx, shared_results, thread_lock)
        threads.append(t)
        t.start()

    # (Ch 2) Join threads (wait for completion)
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Multithreading processing complete. Primes found: {len(shared_results)}")
    print(f"Multithreading time = {end_time - start_time:.4f}")

# --- Multiprocessing Execution (Chapter 3) ---
def run_multiprocessing(num_processes):
    print(f"\n--- Running Multiprocessing ({num_processes} processes) ---")
    ranges = calculate_ranges(num_processes)

    start_time = time.time()

    # (Ch 3) Using a Process Pool
    # 'with' ensures the pool is closed and joined automatically (Context Manager)
    with multiprocessing.Pool(processes=num_processes) as pool:
        # (Ch 3) Map the task function (imported from process_utils) to the input ranges
        # The pool distributes the work and collects the results.
        pool_outputs = pool.map(process_task, ranges)

    end_time = time.time()

    # Flatten the results (Pool.map returns a list of lists)
    mp_results = [item for sublist in pool_outputs for item in sublist]

    print(f"Multiprocessing processing complete. Primes found: {len(mp_results)}")
    print(f"Multiprocessing time = {end_time - start_time:.4f}")


if __name__ == "__main__":
    # (Ch 3) Protection required for multiprocessing, especially on Windows
    multiprocessing.freeze_support()
    
    print("===== PARALLEL PERFORMANCE COMPARISON TEST =====")
    prepare_environment()

    # (Ch 1) Basic Input/Output and error handling
    try:
        # Get user input
        default_count = multiprocessing.cpu_count()
        p_count_input = input(f"Enter number of processes (Default: {default_count}): ")
        t_count_input = input(f"Enter number of threads (Default: {default_count}): ")
        
        p_count = int(p_count_input) if p_count_input else default_count
        t_count = int(t_count_input) if t_count_input else default_count

        if p_count <= 0 or t_count <= 0:
            raise ValueError("Count must be greater than 0.")

    except ValueError as e:
        print(f"Invalid input: {e}. Exiting.")
        exit(1)

    # Run the tests
    run_serial()
    run_multithreading(t_count)
    run_multiprocessing(p_count)
    
    # Final message (Updated: Removed reference to Chapter 4)
    print("\nTest complete. You can inspect 'calculation_log.txt' for File I/O details.")
