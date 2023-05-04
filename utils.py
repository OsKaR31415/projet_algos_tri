from linked_list import List
from random import randint
from math import sqrt
from time import time

def iota(n: int) -> List:
    """
    Tests:
        >>> iota(0)
        List()
        >>> iota(1)
        List(1)
        >>> iota(5)
        List(1, 2, 3, 4, 5)
    """
    if n < 0:
        raise ValueError("n must be positive.")
    if n == 0:
        return List()
    new_list = List()
    while n > 0:
        new_list.prepend(n)
        n -= 1
    return new_list

def reverse_iota(n: int) -> List:
    """
    Tests:
        >>> reverse_iota(0)
        List()
        >>> reverse_iota(1)
        List(1)
        >>> reverse_iota(5)
        List(5, 4, 3, 2, 1)
    """
    return List(*reversed(range(1, n+1)))

def random_list(length: int, max_number: int =100):
    new_list = List()
    for _ in range(length):
        new_list.prepend(randint(1, max_number))
    return new_list

def List_reduce(lst: List, func, init):
    if lst.is_empty():
        return init
    return func(lst.value,
                List_reduce(lst.next, func, init))

def is_sorted(lst: List) -> bool:
    """
    Tests:
        >>> is_sorted(List())
        True
        >>> is_sorted(List(6))
        True
        >>> is_sorted(List(6, 28))
        True
        >>> is_sorted(List(6, 6, 28, 42))
        True
        >>> is_sorted(List(6, 6, 28, 42, 37))
        False
        >>> is_sorted(List(6, 37, 28, 42))
        False
    """
    while (not lst.is_empty()) and not lst.next.is_empty():
        if lst.value > lst.next.value:
            return False
        lst = lst.next
    return True

def average(lst: List or list) -> float:
    """
    Tests:
        >>> average(List(7))
        7.0
        >>> average(List(1, 2, 3, 4, 5, 6))
        3.5
        >>> average([7])
        7.0
        >>> average([1, 2, 3, 4, 5, 6])
        3.5
    """
    return sum(lst) / len(lst)

def std_dev(lst: List or list) -> float:
    """Standard deviation."""
    avg = average(lst)
    sq_dev_to_avg = lambda x: (avg - x)**2
    return sqrt(sum(map(sq_dev_to_avg, lst))) / ( len(lst) - 1 )

def avg_dev(lst: List or list) -> float:
    """Average deviation."""
    avg = average(lst)
    dev_to_avg = lambda x: abs(avg - x)
    return sum(map(dev_to_avg, lst)) / len(lst)


def execution_time(function, *args, **kwargs) -> tuple:
    """Return the execution time of `function` called with the arguments passed
    after it (*args and **kwargs)."""
    dep = time()
    function(*args, **kwargs)
    end = time()
    return end-dep

def return_execution_time(function):
    """Decorator to measure and return the execution time of a function."""
    def wrapper(*args, **kwargs):
        dep = time()
        function(*args, **kwargs)
        end = time()
        return end-dep
    return wrapper


if __name__ == '__main__':
    print(std_dev([0, 2]))


