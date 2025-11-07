# src/mpi_execution.py
# Run using: mpiexec -n 4 python src/mpi_execution.py

try:
    from mpi4py import MPI
except ImportError:
    print("mpi4py not installed. Skipping MPI execution.")
    # Exit with a non-zero status to indicate failure/skip
    exit(1)
    
import time
from analyzer import PrimeAnalyzer

MAX_NUM = 200000

if __name__ == "__main__":
    # Initialize MPI environment (Chap 4)
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank() # Get the rank (ID) of the current process
    size = comm.Get_size() # Get the total number of processes

    # Root process (Rank 0) handles timing and final output
    if rank == 0:
        print(f"--- MPI Execution ---")
        print(f"Analyzing up to {MAX_NUM} with {size} MPI processes...")
        start_time = time.time()

    # Divide the work based on rank (Manual distribution)
    chunk_size = MAX_NUM // size
    my_start = rank * chunk_size
    
    # Ensure the last process covers the remaining range
    if rank == size - 1:
        my_end = MAX_NUM
    else:
        my_end = (rank + 1) * chunk_size

    # Handle the start index adjustment
    if my_start == 0:
        my_start = 1

    # Each process works on its own chunk independently
    analyzer = PrimeAnalyzer()
    local_primes = analyzer.calculate_in_range(my_start, my_end)

    # Collective Communication: Gather results at the root process (rank 0) (Chap 4)
    # All processes send their local_primes, and Rank 0 receives a list of lists.
    all_primes_lists = comm.gather(local_primes, root=0)

    # Finalize results only in the root process
    if rank == 0:
        # Flatten the list of lists received from gather
        final_results = [item for sublist in all_primes_lists for item in sublist]
        end_time = time.time()

        print("-" * 30)
        print(f"MPI Execution Time: {end_time - start_time:.4f} seconds")
        print(f"Total primes found: {len(final_results)}")
        print("-" * 30)
