# 🧮 Parallel Performance Comparison: Prime Number Analysis

## 📘 Description

This Python project compares the performance of different execution models: **Serial (Ch 1)**, **Multithreading (Ch 2)**, **Multiprocessing (Ch 3)**, and **MPI (Ch 4)**. The comparison is based on a CPU-intensive task: calculating prime numbers up to a defined limit (200,000). The core logic utilizes **Object-Oriented Programming and Python Basics (Ch 1)**.

The project is structured by chapter folders to clearly demonstrate the specific concepts taught in the course.

## ⚙️ How It Works

1.  **Core Logic (Ch 1)**: `Chapter1_Basics_OOP/analyzer.py` defines the `PrimeAnalyzer` class, using loops (for/while) and conditionals (if/else) to find primes. It also demonstrates basic File I/O by writing to `calculation_log.txt`.
2.  **Threading (Ch 2)**: `Chapter2_Threading/thread_utils.py` defines a custom `ThreadWorker` class. It demonstrates `threading.Lock` (synchronization) to safely update shared results.
3.  **Multiprocessing (Ch 3)**: `Chapter3_Multiprocessing/process_utils.py` provides a helper function for use with `multiprocessing.Pool` and `map`.
4.  **Main Comparison**: `main_comparison.py` runs the Serial, Multithreading, and Multiprocessing tests.
    *   The user enters the number of threads and processes.
    *   The script measures and compares the execution time for each approach.
5.  **MPI (Ch 4)**: `Chapter4_MPI/mpi_test.py` runs the task using MPI, demonstrating `rank`, `size`, and `gather`. This must be run separately.

## 🧠 System Setup

*   **Language:** Python 3.x
*   **Modules Used:** `time`, `threading`, `multiprocessing`, `os`, `mpi4py`, `numpy`.

### Installation

1. Clone the repository:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd Parallel-Performance-Comparison

2. pip install -r requirements.txt 
