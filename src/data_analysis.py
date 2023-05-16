from typing import Callable
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from cycler import cycler
from random import choice
from utils import average, std_dev
from pprint import pprint

ALGORITHMS_NAMES = [
        # 'recursive_insertion_sort',
        # 'iterative_insertion_sort',
        'bubble_sort',
        'in_place_bubble_sort',
        # 'bucket_sort',
        # 'merge_sort',
        # 'quick_sort'
        ]
FRENCH_ALGO_NAMES = [
        # 'tri par insertion récursive',
        # 'tri par insertion itérative',
        'tri à bulles',
        'tri à bulles en place',
        # 'tri par seaux',
        # 'tri fusion',
        # 'tri rapide'
        ]


with open("saved_statistics/data", "r") as data_file:
    file = data_file.read()
    file = file.split("\n")
    data: dict[dict[dict[list[float]]]] = dict()
    for line in file:
        if line == "": continue
        list_type: str  # the type of list (random_list, iota or reverse_iota)
        algo_name: str  # the algorithm used (quick_sort, bubble_sort...)
        list_length: int  # the length of the list
        timings: list[float]  # the actual data : timings
        list_type, algo_name, list_length, timings = line.split(":")
        list_length = int(list_length)
        timings = [0] if timings == '' else list(map(float, timings.split(",")))
        if data.get(list_type) is None:
            data[list_type] = dict()
        if data[list_type].get(algo_name) is None:
            data[list_type][algo_name] = dict()
        data[list_type][algo_name][list_length] = timings

def random_color():
    # COLOR_TABLE = mcolors.CSS4_COLORS
    COLOR_TABLE = mcolors.XKCD_COLORS
    return choice(list(COLOR_TABLE.values()))


def select_list_type(data: dict[dict[dict[list[float]]]],
                     list_type: str):
    """
    Input: list_type -> algo_name -> list_length -> list[float]
    Output: algo_name -> list_length -> list[float]
    """
    return data[list_type]

def select_algo_name(data: dict[dict[dict[list[float]]]],
                     algo_name: str):
    """
    Input: list_type -> algo_name -> list_length -> list[float]
    Output: list_type -> list_length -> list[float]
    """
    return {list_type: value[algo_name]
            for list_type, value in data.items()}

def select_list_length(data: dict[dict[dict[list[float]]]],
                       list_length: int):
    """
    Input: list_type -> algo_name -> list_length -> list[float]
    Output: list_type -> algo_name -> list[float]
    """
    return {list_type: value[algo_name][list_length]
            for list_type, value in data.items()
            for algo_name in value.keys()}

def aggregate(data: dict, aggregator: Callable, depth: int =1) -> dict:
    if depth == 0:
        aggregated = data
    elif depth == 1:
        aggregated = {key: aggregator(value)
                      for key, value in sorted(data.items())}
    else:
        aggregated = {key: aggregate(value, aggregator, depth - 1)
                      for key, value in data.items()}
    return aggregated

def join(data: dict, depth: int =1) -> list:
    if depth == 0:
        return data
    if depth == 1:
        return list(data.values())
    result = []
    return [join(value, depth-1) for value in sorted(data.values())]

def zeroes_to_nan(lst: list[int | float]) -> list[int | float]:
    return list(map(lambda x: float('nan') if x == 0 else x, lst))


# colors_cycler = cycler(color=['xkcd:black',
#                               'xkcd:electric blue',
#                               'xkcd:light blue',
#                               'xkcd:teal',
#                               'xkcd:green',
#                               'xkcd:light green',
#                               'xkcd:periwinkle',
#                               'xkcd:lilac',
#                               'xkcd:purple',
#                               'xkcd:pink',
#                               'xkcd:pink purple',
#                               'xkcd:slate blue',
#                               'xkcd:gold',
#                               'xkcd:red',
#                               ])
colors = cycler(color=mpl.colormaps['tab10'](range(20)))
plt.rc('lines', linewidth=2)
plt.rc('axes', prop_cycle=colors)


french_for = {
        "reverse_iota": "liste décroissante",
        "iota": "liste croissante",
        "rand_list": "liste aléatoire"
        }
for list_type in ("rand_list", "iota", "reverse_iota",):
    for algo_name, french_name in zip(ALGORITHMS_NAMES, FRENCH_ALGO_NAMES):
        averages = (aggregate(data[list_type][algo_name],
                              average,
                              1))
        averages = join(averages)
        averages = zeroes_to_nan(averages)
        std_devs = join(aggregate(data[list_type][algo_name],
                                  std_dev,
                                  1))
        std_devs = zeroes_to_nan(std_devs)
        areas = list(map(lambda r: r,
                         std_devs))
        X_ticks = list(sorted(data[list_type][algo_name].keys()))
        plt.plot(X_ticks, averages,
                 label=french_name + ", " + french_for[list_type],
                 alpha=0.6)
        plt.scatter(X_ticks, averages, marker="o", s=areas, alpha=0.5)

plt.legend(loc="upper center")

# plt.savefig("../img/final/random_list.png")
plt.show()


