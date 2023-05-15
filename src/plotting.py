import matplotlib.pyplot as plt
from random import random
import pickle
from pprint import pprint
from statistics import TESTED_LENGTHS

ALGORITHMS_NAMES = ['recursive_insertion_sort', 'iterative_insertion_sort',
                    'bubble_sort', 'in_place_bubble_sort', 'bucket_sort',
                    'merge_sort', 'quick_sort']

ALGORITHMS_NAMES = ['bucket_sort', 'quick_sort', 'bubble_sort']

title = " ".join(ALGORITHMS_NAMES) + " random_list"
file_name = 'saved_statistics/' + title + '.pkl'
with open(file_name, 'rb') as file:
    data = pickle.load(file)
    print("data from", file_name, ":")
    pprint(data)


def plot_timings(algo_name: str):
    color = (random(), random(), random())
    widths = (data[algo_name + " std"] * 100) **2
    plt.plot(TESTED_LENGTHS, data[algo_name + " avg"], color=color, label=algo_name)
    plt.scatter(TESTED_LENGTHS, data[algo_name + " avg"], s=widths, color=color)

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


plt.show()

