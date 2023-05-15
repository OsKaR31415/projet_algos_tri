"""
This is the "quick and dirty part of the code"
"""

from typing import Callable
from itertools import zip_longest
import numpy as np
from random import random
from utils import *
from insertion_sort import recursive_insertion_sort, iterative_insertion_sort
from bubble_sort import bubble_sort, in_place_bubble_sort
from bucket_sort import bucket_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

import pickle  # data serializing

from pprint import pprint

# from sys import setrecursionlimit
# setrecursionlimit(1500)  # change the maximum number of recursive calls


SAMPLES_PER_TEST: int = 3

TESTED_LENGTHS: list[int]
# TESTED_LENGTHS = np.logspace(1, 4, 20, dtype=int)
TESTED_LENGTHS = (10, 100, 1000, 10000, 100000)

ALGORITHMS: list[Callable]
# ALGORITHMS = [recursive_insertion_sort, iterative_insertion_sort, bubble_sort,
#               in_place_bubble_sort, bucket_sort, merge_sort, quick_sort]
ALGORITHMS = [bucket_sort, quick_sort, bubble_sort]

ALGORITHMS_NAMES = list(map(lambda x: x.__name__, ALGORITHMS))


################################################################################
# the code after this is not loaded on import
if __name__ == '__main__':

    timings: dict[list[list[float]]] = dict()

    for algo_name, algorithm in zip(ALGORITHMS_NAMES, ALGORITHMS):
        timings[algo_name] = []
        for list_length in TESTED_LENGTHS:
            timings[algo_name].append(test_execution_times(algorithm, iota,
                                                           list_length,
                                                           number_of_samples=SAMPLES_PER_TEST,
                                                           verbose=True))
            # break on call stack overflow or timeout
            # empty list means stack overflow or timeout because all values have
            # been skipped by test_execution_times
            print(timings[algo_name])
            if len(timings[algo_name][-1]) <= 2:
                break
        # make the array of timings a rectangle
        # it is not always a rectangle: some sorting functions can timeout or
        # overflow the call stack
        collector = np.empty((len(TESTED_LENGTHS), SAMPLES_PER_TEST))
        for (i, j), idx in np.ndenumerate(collector):
            try:
                collector[i, j] = timings[algo_name][i][j]
            except IndexError:
                collector[i, j] = 0
        # make it a numpy array
        timings[algo_name] = collector


    # print("  average time  ┃  std deviation  ┃  algorithm name")
    # print("━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━")
    # for times, algo_name in zip(timings, ALGORITHMS_NAMES):
    #     avg = average(times)
    #     std_deviation = std_dev(times)
    #     print("{:015.12f} ┃ {:015.12f} ┃ {}".format(avg, std_deviation,
    #                                                 algo_name))

    stats = dict()
    for name, times in timings.items():
        avg = np.average(times, axis=1)
        std = np.std(times, axis=1)
        stats[name + " avg"] = avg
        stats[name + " std"] = std

    pprint(stats)

    # # save the python object into a binary file
    # title = " ".join(ALGORITHMS_NAMES) + " iota"
    # file_name = 'saved_statistics/' + title + '.pkl'
    # with open(file_name, 'wb') as save_file:
    #     pickle.dump(stats, save_file)
    #     print("data saved into", file_name)
    #     print("\07")  # ring a bell


