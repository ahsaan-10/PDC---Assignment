# Chapter4_MPI/mpi_test.py
# Run this file from the root directory using: mpiexec -n 4 python Chapter4_MPI/mpi_test.py

try:
    from mpi4py import MPI
except ImportError:
    print("mpi4py not installed. Skipping MPI execution.")
    # Exit if mpi4py is not available
    exit(1)
    
import time
import sys
import os

# Add the root directory to the path to ensure imports work correctly when run via mpiexec
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import PrimeAnalyzer from the Chapter 1 package
from Chapter1_Basics_OOP.analyzer import PrimeAnalyzer

MAX_NUM = 200000

if __name__ == "__main__":
    # (Ch 4) Initialize MPI environment (COMM_WORLD includes all processes)
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank() # Get the rank (ID) of the current process
    size = comm.Get_size() # Get the total number of processes

    # (Ch 4) Root process (Rank 0) handles timing and output
    if rank == 0:
        print(f"\n--- Running MPI Execution ({size} processes) ---")
        start_time = time.time()

    # Divide the work based on rank (Manual distribution)
    chunk_size = MAX_NUM // size
    my_start = rank * chunk_size
    
    # Ensure the last process covers the remainder
    if rank == size - 1:
        my_end = MAX_NUM
    else:
        my_end = (rank + 1) * chunk_size

    # Start checking from 1 instead of 0
    if my_start == 0:
        my_start = 1

    # Each process works on its own chunk independently
    analyzer = PrimeAnalyzer()
    local_primes = analyzer.calculate_in_range(my_start, my_end)

    # (Ch 4) Collective Communication: Gather results at the root process (rank 0)
    # All processes send their data, Rank 0 receives a list of lists.
    all_primes_lists = comm.gather(local_primes, root=0)

    # Finalize results only in the root process
    if rank == 0:
        # Flatten the list of lists received from gather
        final_results = [item for sublist in all_primes_lists for item in sublist]
        end_time = time.time()

        print(f"MPI processing complete. Primes found: {len(final_results)}")
        print(f"MPI time = {end_time - start_time:.4f}")
