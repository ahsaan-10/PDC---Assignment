# Chapter3_Multiprocessing/process_utils.py

# Import PrimeAnalyzer from the Chapter 1 package
from Chapter1_Basics_OOP.analyzer import PrimeAnalyzer

# (Ch 3) Helper function for Pool.map. 
# It must be defined at the top level so multiprocessing can pickle (serialize) it.
def process_task(args):
    """
    Function executed by each process in the pool.
    """
    start_idx, end_idx = args
    # Create analyzer instance within the new process memory space
    analyzer = PrimeAnalyzer()
    return analyzer.calculate_in_range(start_idx, end_idx)
