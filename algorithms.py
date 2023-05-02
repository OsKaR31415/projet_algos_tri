from linked_list import List
from utils import *

def recursive_insertion(lst: List, value) -> List:
    if lst.is_empty() or lst.value > value:
        lst.prepend(value)
        return lst
    lst.next = recursive_insertion(lst.next, value)
    return lst

def insertion_sort(lst: List) -> List:
    sorted_lst = List()
    while not lst.is_empty():
        sorted_lst = recursive_insertion(sorted_lst, lst.value)
        lst = lst.next
    return sorted_lst


A = random_list(10)
print(A)
A = insertion_sort(A)
print(A)

