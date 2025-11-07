# src/serial_execution.py
import time
from analyzer import PrimeAnalyzer
import os

# Define the total range to analyze (CPU intensive task)
MAX_NUM = 200000
LOG_FILE = 'execution_log.txt'

if __name__ == "__main__":
    print(f"--- Serial Execution ---")
    print(f"Analyzing numbers up to {MAX_NUM}...")
    analyzer = PrimeAnalyzer()

    start_time = time.time()

    # Perform the calculation
    # We start from 1, as 0 is handled by the is_prime function
    results = analyzer.calculate_in_range(1, MAX_NUM)

    end_time = time.time()

    print("-" * 30)
    print(f"Serial Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Total primes found: {len(results)}")
    print("-" * 30)

    # Chapter 1: File I/O - Writing the count to a log file
    # Ensure we are writing to the file in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, LOG_FILE)
    
    try:
        with open(log_path, 'w') as f:
            f.write(f"Serial run completed.\n")
            f.write(f"Total primes found: {len(results)}\n")
        print(f"Log file '{LOG_FILE}' updated in src directory.")
    except IOError as e:
        print(f"Error writing log file: {e}")
