from typing import Callable
import matplotlib.pyplot as plt
from linked_list import List
from random import randint
from math import sqrt
from time import time


def iota(n: int) -> List:
    """# {{{
    Tests:
        >>> iota(0)
        List()
        >>> iota(1)
        List(1)
        >>> iota(5)
        List(1, 2, 3, 4, 5)
    """  # }}}
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
    """# {{{
    Tests:
        >>> reverse_iota(0)
        List()
        >>> reverse_iota(1)
        List(1)
        >>> reverse_iota(5)
        List(5, 4, 3, 2, 1)
    """  # }}}
    return List(*reversed(range(1, n+1)))


def random_list(length: int, max_number: int = 100) -> List:
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
    """# {{{
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
    """  # }}}
    while (not lst.is_empty()) and not lst.next.is_empty():
        if lst.value > lst.next.value:
            return False
        lst = lst.next
    return True


def average(lst: List or list) -> float:
    """# {{{
    Tests:
        >>> average(List(7))
        7.0
        >>> average(List(1, 2, 3, 4, 5, 6))
        3.5
        >>> average([7])
        7.0
        >>> average([1, 2, 3, 4, 5, 6])
        3.5
    """  # }}}
    return sum(lst) / len(lst)


def std_dev(lst: List or list) -> float:
    """Standard deviation."""
    avg = average(lst)
    def sq_dev_to_avg(x): return (avg - x)**2
    return sqrt(sum(map(sq_dev_to_avg, lst))) / (len(lst) - 1)


def avg_dev(lst: List or list) -> float:
    """Average deviation."""
    avg = average(lst)
    def dev_to_avg(x): return abs(avg - x)
    return sum(map(dev_to_avg, lst)) / len(lst)


def execution_time(function: Callable, *args, **kwargs) -> float:
    """Return the execution time of `function` called with the arguments passed
    after it (*args and **kwargs)."""
    dep = time()
    function(*args, **kwargs)
    end = time()
    return end - dep


def return_execution_time(function: Callable) -> float:
    """Decorator to measure and return the execution time of a function."""
    def wrapper(*args, **kwargs):
        dep = time()
        try:
            function(*args, **kwargs)
        except Exception as e:
            return e
        end = time()
        return end - dep
    return wrapper

def test_execution_times(sorting_function: Callable[List, List],
                         random_list_function: Callable[int, List],
                         number_of_tests: int =100,
                         verbose: bool =False) -> list[float]:
    """Return a list of execution times for sorting lists generated using# {{{
    `random_list_function` with `sorting_function`.
    Args:
        sorting_function (Callable[List, List]): The function used to sort Lists.
        random_list_function (Callable[int, List]): The function used to generate
            the lists to sort. This is a function that takes a number and returns a List of integers.
        number_of_tests (int): The numbers of tests to run. Each test is on a
            list of 100 more elements than the previous, so the maximum number
            of tested values is `100 * number_of_tests`.
        verbose (bool): Wether to pring log during the tests.
    """# }}}
    if verbose:
        print("-" * 50)
        print(f"testing {sorting_function.__name__} on {number_of_tests} lists generated using {random_list_function.__name__}")
    time_to_sort = return_execution_time(sorting_function)
    timings = []
    for length in range(100, 100*number_of_tests, 100):
        sorting_time = time_to_sort(random_list_function(length))
        if isinstance(sorting_time, RecursionError):
            print("recursion error, stopping tests here")
            break
        timings.append(sorting_time)
        if verbose:
            print(sorting_time)
    if verbose:
        print("values :", timings)
    return timings


def plot_execution_times(sorting_function: Callable[List, List],
                         number_of_tests: int =100,
                         verbose: bool =False):
    rand_lst_times = test_execution_times(sorting_function, random_list,
                                          number_of_tests, verbose)
    inc_lst_times = test_execution_times(sorting_function, iota,
                                         number_of_tests, verbose)
    dec_lst_times = test_execution_times(sorting_function, reverse_iota,
                                         number_of_tests, verbose)
    plt.plot(rand_lst_times, color="green")
    plt.plot(inc_lst_times,  color="blue")
    plt.plot(dec_lst_times,  color="red")
    plt.show()



if __name__ == '__main__':
    from bucket_sort import bucket_sort
    plot_execution_times(bucket_sort, 20, True)


