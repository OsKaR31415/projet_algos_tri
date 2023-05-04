from typing import Callable
from linked_list import List
from node import Node
from utils import *

def recursive_insertion(lst: List, value) -> List:
    if lst.is_empty() or lst.value > value:
        lst.prepend(value)
        return lst
    lst.next = recursive_insertion(lst.next, value)
    return lst

def iterative_insertion(lst: List, value) -> List:
    new_list = List(True)  # List containing a foo value
    tail = new_list # Last node of the list
    value_inserted = False  # is the value already inserted ?
    for elt in lst:
        if (not value_inserted) and value < elt:
            tail.next = List(value)
            tail = tail.next
            value_inserted = True  # now the value has bee inserted
        tail.next = List(elt)
        tail = tail.next
    if not value_inserted:
        tail.next = List(value)
    new_list = new_list.next  # remove the useless first element
    return List(new_list)

def insertion_sort(insertion_function: Callable[List, List], lst: List) -> List:
    sorted_lst = List(1)
    while not lst.is_empty():
        sorted_lst = insertion_function(sorted_lst, lst.value)
        lst = lst.next
    return sorted_lst

def recursive_insertion_sort(lst: List) -> List:
    return insertion_sort(recursive_insertion, lst)

def iterative_insertion_sort(lst: List) -> List:
    return insertion_sort(iterative_insertion, lst)

@return_execution_time
def time_iterative_insertion_sort(sample: List) -> float:
    iterative_insertion_sort(sample)

@return_execution_time
def time_recursive_insertion_sort(sample: List) -> float:
    recursive_insertion_sort(sample)


A = random_list(10)
# print(recursive_insertion_sort(A))
# print(A)
print(is_sorted(iterative_insertion_sort(A)))


