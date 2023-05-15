from linked_list import List
from utils import *

def merge(a: List, b: List) -> List:
    """Merge two already sorted lists into one sorted list.
    Tests:
        >>> merge(List(2, 7, 8, 10), List(1, 1, 1, 4, 5, 11))
        List(1, 1, 1, 2, 4, 5, 7, 8, 10, 11)
    """
    if a.is_empty():
        return b
    if b.is_empty():
        return a
    result = List(True)  # list with a foo initial element
    result_tail = result
    while not (a.is_empty() or b.is_empty()):
        if a.value < b.value:
            maximum = a.value
            a = a.next
        else:
            maximum = b.value
            b = b.next
        result_tail.next = List(maximum)
        result_tail = result_tail.next
    if not a.is_empty():
        result_tail.next = a
    elif not b.is_empty():
        result_tail.next = b
    # delete the initial foo value
    result = result.next
    return result


def merge_sort(lst: List) -> List:
    """# {{{
    Tests:
        >>> all(is_sorted(merge_sort(random_list(n))) for n in range(50))
        True
    """# }}}
    if lst.is_empty():
        return List()
    if lst.next.is_empty():
        return lst
    odd = List()
    even = List()
    index = 0
    while not lst.is_empty():
        if index % 2 == 0:
            even.prepend(lst.value)
        else:
            odd.prepend(lst.value)
        lst = lst.next
        index += 1
    return merge(merge_sort(even), merge_sort(odd))

if __name__ == "__main__":
    print_data_for(merge_sort)



