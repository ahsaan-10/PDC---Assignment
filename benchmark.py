# benchmark.py
"""Repeatable benchmark: serial vs threads vs processes for several worker counts.

Usage:
    python benchmark.py                 # 5 repeats, workers 1 2 4 8
    python benchmark.py --repeats 3 --workers 2 4 --max 2000000

Prints a Markdown table of median wall-clock times and speed-ups versus serial.
"""

import argparse
import multiprocessing
import platform
import statistics
import threading
import time

from Chapter1_Basics_OOP.analyzer import PrimeAnalyzer
from Chapter2_Threading.thread_utils import ThreadWorker
from Chapter3_Multiprocessing.process_utils import process_task
import main_comparison
from main_comparison import calculate_ranges, prepare_environment


def time_serial():
    start = time.perf_counter()
    count = len(PrimeAnalyzer().calculate_in_range(1, main_comparison.MAX_NUM))
    return time.perf_counter() - start, count


def time_threads(n):
    results, lock = [], threading.Lock()
    workers = [ThreadWorker(f"T{i}", s, e, results, lock) for i, (s, e) in enumerate(calculate_ranges(n))]
    start = time.perf_counter()
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    return time.perf_counter() - start, len(results)


def time_processes(n):
    start = time.perf_counter()
    with multiprocessing.Pool(processes=n) as pool:
        chunks = pool.map(process_task, calculate_ranges(n))
    return time.perf_counter() - start, sum(len(c) for c in chunks)


def median_time(fn, repeats, *args):
    times, counts = [], set()
    for _ in range(repeats):
        t, c = fn(*args)
        times.append(t)
        counts.add(c)
    assert len(counts) == 1, f"inconsistent prime counts: {counts}"
    return statistics.median(times), counts.pop()


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--workers", type=int, nargs="+", default=[1, 2, 4, 8])
    parser.add_argument("--max", type=int, default=main_comparison.MAX_NUM, help="upper end of the range")
    args = parser.parse_args()

    main_comparison.MAX_NUM = args.max
    prepare_environment()
    serial, primes = median_time(time_serial, args.repeats)

    print(f"Python {platform.python_version()} on {platform.system()}, "
          f"{multiprocessing.cpu_count()} logical CPUs, range 1-{main_comparison.MAX_NUM:,}, "
          f"median of {args.repeats} runs, {primes:,} primes found by every mode\n")
    print("| Workers | Serial (s) | Threads (s) | Processes (s) | Thread speed-up | Process speed-up |")
    print("| ---: | ---: | ---: | ---: | ---: | ---: |")
    for n in args.workers:
        t, tc = median_time(time_threads, args.repeats, n)
        p, pc = median_time(time_processes, args.repeats, n)
        assert tc == pc == primes, "modes disagree on the number of primes"
        print(f"| {n} | {serial:.3f} | {t:.3f} | {p:.3f} | {serial / t:.2f}x | {serial / p:.2f}x |")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
