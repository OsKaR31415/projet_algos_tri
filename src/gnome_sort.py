from linked_list import List
from utils import *

def recursive_gnome_sort(lst: List, rest: List =None):
    """# {{{
    Tests:
        >>> all(is_sorted(recursive_gnome_sort(random_list(n))) for n in range(50))
        True
    """# }}}
    if rest is None:
        rest = List(lst.value)
        lst = lst.cdr()
    if lst.is_empty():
        return rest
    if rest.is_empty():
        rest.prepend(lst.car())
        lst = lst.cdr()
        return gnome_sort(lst, rest)
    if lst.value > rest.value:
        lst.value, rest.value = rest.value, lst.value
        lst.prepend(rest.car())
        return gnome_sort(lst, rest.cdr())
    else:
        rest.prepend(lst.car())
        return recursive_gnome_sort(lst.cdr(), rest)

# def iterative_gnome_sort(lst: List):
#     """# {{{
#     Tests:
#         >>> all(is_sorted(iterative_gnome_sort(random_list(n))) for n in range(50))
#         True
#     """# }}}
#     if lst.is_empty():
#         return List()
#     rest = List(lst.value)
#     lst = lst.cdr()
#     while not lst.is_empty():
#         input(str(list(reversed(list(lst)))) + "  " + str(rest))
#         if rest.is_empty() or lst.value > rest.value:
#             lst.value, rest.value = rest.value, lst.value
#             rest.prepend(lst.car())
#             lst = lst.next
#         else:
#             lst.prepend(rest.car())
#             rest = rest.next
#     return rest, lst


@return_execution_time
def time_recursive_gnome_sort(sample: List) -> float:
    recursive_gnome_sort(sample)

# @return_execution_time
# def time_iterative_gnome_sort(sample: List) -> float:
#     iterative_gnome_sort(sample)

if __name__ == "__main__":
    ...

