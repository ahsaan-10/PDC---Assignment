# 🧮 Parallel Performance Comparison: Prime Number Analysis

## 📘 Description

This Python project compares the performance of different execution models: **Serial (Ch 1)**, **Multithreading (Ch 2)**, and **Multiprocessing (Ch 3)**. The comparison is based on a CPU-intensive task: calculating prime numbers up to a defined limit (200,000). The core logic utilizes **Object-Oriented Programming and Python Basics (Ch 1)**.

The project is structured by chapter folders to clearly demonstrate the specific concepts taught in the course.

## ⚙️ How It Works

1.  **Core Logic (Ch 1)**: `Chapter1_Basics_OOP/analyzer.py` defines the `PrimeAnalyzer` class, using loops (for/while) and conditionals (if/else) to find primes. It also demonstrates basic File I/O by writing to `calculation_log.txt`.
2.  **Threading (Ch 2)**: `Chapter2_Threading/thread_utils.py` defines a custom `ThreadWorker` class. It demonstrates `threading.Lock` (synchronization) to safely update shared results.
3.  **Multiprocessing (Ch 3)**: `Chapter3_Multiprocessing/process_utils.py` provides a helper function for use with `multiprocessing.Pool` and `map`.
4.  **Main Comparison**: `main_comparison.py` orchestrates the tests.
    *   The user enters the number of threads and processes.
    *   The script measures and compares the execution time for each approach.

## 📂 Repository Structure

/ ├── README.md ├── main_comparison.py ├── calculation_log.txt (Generated during execution) │ ├── Chapter1_Basics_OOP/ │ ├── analyzer.py │ ├── Chapter2_Threading/ │ ├── thread_utils.py │ └── Chapter3_Multiprocessing/ └── process_utils.py

*(Note: Empty `__init__.py` files are present in the chapter folders to allow them to be imported as packages.)*

## 🧠 System Setup

*   **Language:** Python 3.x
*   **Modules Used:** `time`, `threading`, `multiprocessing`, `os` (all built-in).

### Installation

No external packages are required. You only need Python installed.

1. Clone the repository:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd Parallel-Performance-Comparison

   🚀 How to Run
Run the main comparison script from the root directory of the project.

Bash

python main_comparison.py
(Or use py main_comparison.py on some Windows systems).

You will be prompted to enter the number of processes and threads.

📊 Experimental Results (Example Data)
The following results are examples obtained on a multi-core CPU analyzing numbers up to 200,000. Results will vary based on your hardware.

🔹 Case: 4 Workers (Processes/Threads)
main_comparison.py Output (Simulated):

===== PARALLEL PERFORMANCE COMPARISON TEST =====
Enter number of processes (Default: 4): 4
Enter number of threads (Default: 4): 4

--- Running Serial Execution ---
Serial processing complete. Primes found: 17984
Serial time = 0.3550

--- Running Multithreading (4 threads) ---
Multithreading processing complete. Primes found: 17984
Multithreading time = 0.4820

--- Running Multiprocessing (4 processes) ---
Multiprocessing processing complete. Primes found: 17984
Multiprocessing time = 0.1520

📊 Comparison TableExecution MethodTime (s) (Example)Concepts AppliedSerial0.3550sCh 1: OOP, Control Flow, File I/OMultithreading (4T)0.4820sCh 2: Threads, Locks, SynchronizationMultiprocessing (4P)0.1520sCh 3: Process Pool, Map

💡 Conclusion
Ch 1 (Serial) Performance: This serves as the baseline, utilizing only a single CPU core.

Ch 2 (Multithreading) Performance: Multithreading was observed to be slower than or similar to serial execution. This is due to Python's Global Interpreter Lock (GIL), which prevents true parallel execution of threads for CPU-heavy tasks. The overhead of thread management and synchronization (Locks) adds to the time.

Ch 3 (Multiprocessing) Performance: Multiprocessing was the fastest method. It bypasses the GIL by creating separate processes, utilizing multiple CPU cores effectively.

Final Verdict: For CPU-bound operations in Python (like heavy mathematical calculations), Multiprocessing (Ch 3) is the preferred method over Threading (Ch 2).
