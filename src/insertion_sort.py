from typing import Callable
from linked_list import List
from utils import *

def recursive_insertion(lst: List, value) -> List:
    """# {{{
    Tests:
        >>> recursive_insertion(List(1), 2)
        List(1, 2)
        >>> recursive_insertion(List(1), 0)
        List(0, 1)
        >>> all(is_sorted(recursive_insertion(iota(50), n)) for n in range(51))
        True
    """# }}}

    if lst.is_empty() or lst.value > value:
        lst.prepend(value)
        return lst
    lst.next = recursive_insertion(lst.next, value)
    return lst

def iterative_insertion(lst: List, value) -> List:
    """# {{{
    Tests:
        >>> iterative_insertion(List(1), 2)
        List(1, 2)
        >>> iterative_insertion(List(1), 0)
        List(0, 1)
        >>> all(is_sorted(iterative_insertion(iota(50), n)) for n in range(51))
        True
    """# }}}

    new_list = List(False)  # List containing a foo value
    tail = new_list  # Last node of the list
    lst_ptr = lst  # pointer to the current element of lst
    # /!\ order of conditions in the while is important :
    # you need to test that lst_ptr is not empty before getting its value.
    while (not lst_ptr.is_empty()) and (value > lst_ptr.value):
        # copy the current lst_ptr.value at the end of the new list
        tail.next = List(lst_ptr.value)
        tail = tail.next
        lst_ptr = lst_ptr.next
    tail.next = List(value)
    tail.next.next = lst_ptr
    return new_list.cdr()  # skip the useless first element


def insertion_sort(insertion_function: Callable[List, List], lst: List) -> List:
    sorted_lst = List(1)
    while not lst.is_empty():
        sorted_lst = insertion_function(sorted_lst, lst.value)
        lst = lst.next
    return sorted_lst

def recursive_insertion_sort(lst: List) -> List:
    """# {{{
    Tests:
        >>> all(is_sorted(recursive_insertion_sort(random_list(n))) for n in range(50))
        True
    """# }}}
    return insertion_sort(recursive_insertion, lst)

def iterative_insertion_sort(lst: List) -> List:
    """# {{{
    Tests:
        >>> all(is_sorted(recursive_insertion_sort(random_list(n))) for n in range(50))
        True
    """# }}}
    return insertion_sort(iterative_insertion, lst)

@return_execution_time
def time_iterative_insertion_sort(sample: List) -> float:
    iterative_insertion_sort(sample)

@return_execution_time
def time_recursive_insertion_sort(sample: List) -> float:
    recursive_insertion_sort(sample)


if __name__ == "__main__":
    for num_values in (10, 100, 1000, 2000):
        R = random_list(num_values)
        print(time_recursive_insertion_sort(R))
        print(time_iterative_insertion_sort(R))



