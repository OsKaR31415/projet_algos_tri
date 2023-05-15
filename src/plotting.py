import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from random import random, choice
from math import pi
import pickle
from pprint import pprint
from statistics import TESTED_LENGTHS

ALGORITHMS_NAMES = ['recursive_insertion_sort', 'iterative_insertion_sort',
                    'bubble_sort', 'in_place_bubble_sort', 'bucket_sort',
                    'merge_sort', 'quick_sort']

# ALGORITHMS_NAMES = ['bucket_sort', 'quick_sort', 'bubble_sort']

title = "all reverse_iota 200s"
file_name = 'saved_statistics/' + title + '.pkl'

with open(file_name, 'rb') as file:
    data = pickle.load(file)
    print("data from", file_name, ":")
    pprint(data)


def find(lst, value):
    """Find the index of first occurrence of `value` in `lst`.
    Return -1 if `value` is not in `lst`."""
    for idx, elt in enumerate(lst):
        if elt == value:
            return idx
    return -1

def random_color():
    # COLOR_TABLE = mcolors.CSS4_COLORS
    COLOR_TABLE = mcolors.XKCD_COLORS
    return choice(list(COLOR_TABLE.values()))

def plot_timings(algo_name: str):
    # remove zeroes
    last_idx = find(data[algo_name + " avg"], 0)
    data[algo_name + " std"] = data[algo_name + " std"][:last_idx]
    data[algo_name + " avg"] = data[algo_name + " avg"][:last_idx]
    color = random_color()
    areas = (data[algo_name + " std"] * pi) ** 2  # area from the radius
    plt.plot(TESTED_LENGTHS[:last_idx], data[algo_name + " avg"], color=color, label=algo_name)
    plt.scatter(TESTED_LENGTHS[:last_idx], data[algo_name + " avg"], s=areas, color=color)

    # plt.plot(data[algo_name + " avg"], label=algo_name, color=color)

for algo_name in ALGORITHMS_NAMES:
    plot_timings(algo_name)

plt.legend(loc="upper left")
# plt.xticks(list(range(len(TESTED_LENGTHS))),
#            TESTED_LENGTHS)

# for algo_name in ALGORITHMS_NAMES:
#     plt.boxplot(timings[algo_name])
# plt.xticks(list(range(len(TESTED_LENGTHS))), TESTED_LENGTHS)

# for line, algorithm in zip(timings, ALGORITHMS):
#     plt.plot(line, label=algorithm.__name__)
# legend = plt.legend(loc="upper left")


plt.savefig("../img/" + title, dpi=500)
plt.show()


