# Parallel Prime Analyzer: A Comparative Tutorial

This project demonstrates various methods of parallel programming in Python, combining concepts from an introductory course covering Basics (Ch 1), Threading (Ch 2), Multiprocessing (Ch 3), and MPI (Ch 4).

The objective is to calculate prime numbers up to a specific limit (`MAX_NUM = 200000`) using different techniques and compare their execution times and implementation methods.

## Concepts Covered

| Chapter | Concepts Demonstrated | Implementation Location |
| :--- | :--- | :--- |
| **Ch 1: Basics & OOP** | Classes, `__init__`, Control Flow (if/while/for), File I/O, Serial execution. | `src/analyzer.py`, `src/serial_execution.py` |
| **Ch 2: Threading** | Creating Threads, `start()`, `join()`, Synchronization using `threading.Lock` to prevent race conditions. | `src/threaded_execution.py` |
| **Ch 3: Multiprocessing** | Spawning Processes, `multiprocessing.Pool`, `pool.map` for efficient distribution, Bypassing the GIL. | `src/multiprocess_execution.py` |
| **Ch 4: MPI** | Using `mpi4py`, Communicator, Rank, Size, Collective communication (`comm.gather`). | `src/mpi_execution.py` |

## Repository Structure
├── README.md 
├── requirements.txt 
└── src/ 
   ├── analyzer.py # Core logic (OOP/Prime checking) 
   ├── serial_execution.py # Baseline implementation 
   ├── threaded_execution.py # Threading with Locks 
   ├── multiprocess_execution.py # Multiprocessing with Pool.map 
   └── mpi_execution.py # MPI with Gather

## Setup and Installation

### Prerequisites
1. Python 3.x installed.
2. For the MPI execution (Ch 4), you need an MPI implementation (like OpenMPI or MPICH) installed on your system.

### Instructions

1. **Clone the repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd Parallel-Prime-Analyzer

2. **pip install -r requirements.txt**
