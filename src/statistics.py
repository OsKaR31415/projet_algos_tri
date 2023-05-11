import matplotlib.pyplot as plt
from itertools import zip_longest
from utils import *
from insertion_sort import recursive_insertion_sort, iterative_insertion_sort
from bubble_sort import bubble_sort, in_place_bubble_sort
from bucket_sort import bucket_sort

timings = []

for algorithm in [recursive_insertion_sort, iterative_insertion_sort,
                  bubble_sort, in_place_bubble_sort, bucket_sort]:
    timings.append(test_execution_times(algorithm, random_list, 20, verbose=True))


for line in timings:
    plt.plot(line)
plt.show()

