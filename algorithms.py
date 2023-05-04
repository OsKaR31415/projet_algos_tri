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
    tail = new_list  # Last node of the list
    lst_ptr = lst  # pointer to the current element of lst
    # /!\ order of conditions in the while is important :
    # you need to test that lst_ptr is not empty before getting its value.
    while (not lst_ptr.is_empty()) and (value > lst_ptr.value):
        tail.next = List(lst_ptr.value)
        tail = tail.next
        lst_ptr = lst_ptr.next
    tail.next = List(value)
    tail.next.next = lst_ptr
    return new_list.cdr()


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
# print(iterative_insertion(iota(5), 6))
print(is_sorted(iterative_insertion_sort(A)))


