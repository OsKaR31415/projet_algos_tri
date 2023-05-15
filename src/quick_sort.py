from linked_list import List
from utils import *


def quick_sort(lst: List, depth=1):
    """# {{{
    Tests:
        >>> all(is_sorted(quick_sort(random_list(n))) for n in range(50))
        True
    """# }}}
    if lst.is_empty():
        return lst
    if lst.next.is_empty():
        return List(lst.value)
    pivot = lst.value
    Linf = List()  # list of elements smaller to the pivot
    Lsup = List()  # list of elements greater than the pivot
    Leq = List()  # list of elements equal to the pivot
    for elt in lst:
        if elt == pivot:
            Leq.prepend(elt)
        elif elt < pivot:
            Linf.prepend(elt)
        else:
            Lsup.prepend(elt)
    Linf = quick_sort(Linf)
    Lsup = quick_sort(Lsup)
    Linf.extend(Leq)
    Linf.extend(Lsup)
    return Linf


if __name__ == '__main__':
    print_data_for(quick_sort)
