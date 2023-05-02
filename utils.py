from linked_list import List
from random import randint

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
    """
    return List(*reversed(range(1, n+1)))

def random_list(length: int):
    new_list = List()
    for _ in range(length):
        new_list.prepend(randint(1, 100))
    return new_list

def List_reduce(lst: List, func, init):
    if lst.is_empty():
        return init
    return func(lst.value,
                List_reduce(lst.next, func, init))

def List_map(lst: List, func):
    if lst.is_empty():
        return List()
    l = List()
    l.value = func(lst.value)
    l.next = List_map(lst.next, func)
    return l

def is_sorted(lst: List) -> bool:
    while (not lst.is_empty()) and not lst.next.is_empty():
        if lst.value > lst.next.value:
            return False
        lst = lst.next
    return True


