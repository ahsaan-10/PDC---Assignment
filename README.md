# Parallel Prime Analyzer

**Benchmarks serial, multithreaded, and multiprocess Python on the same CPU-bound task to show when parallelism actually pays off.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

The program counts prime numbers across a large range in three ways and compares their run times:

| Mode | How it works |
| --- | --- |
| **Serial** | One loop checks every number (the baseline). |
| **Threads** | The range is split across `threading.Thread` workers that write to a shared list protected by a lock. |
| **Processes** | The range is split across a `multiprocessing.Pool`, so each chunk runs in its own Python process. |

Every mode must find the same number of primes; the benchmark checks this before reporting any timing.

## Key findings

- **Threads do not speed up CPU-bound Python.** The Global Interpreter Lock lets only one thread run Python code at a time, so threads were never faster than the serial version.
- **Processes do, once the work is big enough.** On a 4-core laptop with a range of 1.5 million numbers, 4 processes ran about **2× faster** than serial.
- **Small jobs are slower in parallel.** With the default range of 200,000 numbers, starting worker processes cost more time than it saved.

## Getting started

No packages are needed: everything uses the Python standard library.

```bash
git clone https://github.com/ahsaan-10/parallel-prime-analyzer.git
cd parallel-prime-analyzer
```

| Goal | Command |
| --- | --- |
| Interactive comparison (asks for worker counts) | `python main_comparison.py` |
| Repeatable benchmark, Markdown table output | `python benchmark.py` |
| Bigger workload, chosen worker counts | `python benchmark.py --max 1500000 --workers 1 2 4 8 --repeats 3` |

`benchmark.py` reports the **median** of several runs plus speed-up versus serial, along with your Python version and CPU count. Run it on an idle machine for stable numbers.

## Project structure

```text
parallel-prime-analyzer/
├── main_comparison.py           # Interactive comparison of the three modes
├── benchmark.py                 # Repeatable benchmark with median timings
├── Chapter1_Basics_OOP/
│   └── analyzer.py              # PrimeAnalyzer class (6k ± 1 primality test)
├── Chapter2_Threading/
│   └── thread_utils.py          # ThreadWorker with lock-protected shared results
└── Chapter3_Multiprocessing/
    └── process_utils.py         # Worker function for the process pool
```

Each run also writes `calculation_log.txt`, recording the chunk each worker processed.

## Concepts demonstrated

Object-oriented design · threads and locks · process pools · work partitioning · benchmarking methodology (repeats, medians, correctness checks)

## License

Released under the [MIT License](LICENSE).
