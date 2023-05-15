from typing import Callable
from utils import average, std_dev
from pprint import pprint

ALGORITHMS_NAMES = [
        # 'recursive_insertion_sort',
        'iterative_insertion_sort',
        'bubble_sort',
        # 'in_place_bubble_sort',
        'bucket_sort',
        'merge_sort',
        'quick_sort'
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
        aggregated = {key: aggregator(value) for key, value in data.items()}
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
    return [join(value, depth-1) for value in data.values()]

# pprint(data)

for list_type in ("rand_list", "iota", "reverse_iota"):
    for algo_name in ALGORITHMS_NAMES:
        print(algo_name, ":")
        values = aggregate(data[list_type][algo_name],
                           std_dev,
                           1)
        pprint(values)




