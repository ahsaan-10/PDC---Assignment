# Parallel Prime Analyzer

**A Python coursework experiment comparing serial execution, threads, and processes on prime-number calculation.**

## What it demonstrates

- Object-oriented Python through a `PrimeAnalyzer` class.
- Thread workers sharing results under a lock.
- A multiprocessing pool distributing ranges across processes.
- Runtime measurements and file logging.

This is a fundamentals and performance-experiment repository, rather than an AI or predictive data science application.

## Run locally

```bash
git clone https://github.com/ahsaan-10/PDC---Assignment.git
cd PDC---Assignment
python main_comparison.py
```

The main comparison uses Python's standard library. Enter positive process and thread counts when prompted. It checks primes in a range ending at 200,000 and prints counts and durations for each execution mode.

## Repository map

```text
main_comparison.py          Experiment entry point
Chapter1_Basics_OOP/        Prime calculation class
Chapter2_Threading/         Thread worker implementation
Chapter3_Multiprocessing/   Process task helper
```

`calculation_log.txt` is generated when the experiment runs.

## Interpreting the comparison

Use the counts to check that all three modes produce equivalent results. Runtime depends on hardware, interpreter build, worker count, logging, and process startup overhead. Timing examples in the original README were labeled simulated; this README makes no measured speedup claim.

For a stronger experiment, repeat runs, report the Python version and hardware, and summarize the variation rather than relying on one duration.
