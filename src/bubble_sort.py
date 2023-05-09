from typing import Callable
from linked_list import List
from utils import *

def bubble_sort(lst: List, acc: List =None) -> List:
    """# {{{
    Args:
        lst (List): The list to sort
        acc (List): The accumulator, the part of the list that is already
                    sorted. Defaults to List() (empty linked list)
    Tests:
        >>> all(is_sorted(bubble_sort(random_list(n))) for n in range(50))
        True
    """# }}}
    # print("lst =" + str(lst) + "  acc =")  # debug
    if acc is None:
        # you have to set the default value of acc here, otherwise it will be
        # the same for all calls of the function.
        acc = List()
    if lst.is_empty():
        return acc
    if lst.next.is_empty():
        acc.prepend(lst.value)
        return acc
    previous = lst
    current = lst.next
    while (not previous.is_empty()) and (not current.is_empty()):
        # print("->" + str(lst))  # debug
        # bubble up any unsorted pair
        if previous.value > current.value:
            tmp            = previous.value
            previous.value = current.value
            current.value  = tmp
        pre_previous = previous
        previous = previous.next
        current = current.next
    # put the sorted element into the accumulator (last element of lst)
    # it isn't current because current is None (stop condition of the while)
    new_acc = List(previous.value)
    new_acc.next = acc
    # delete the last (newly sorted) element of lst
    del pre_previous.next
    return bubble_sort(lst, new_acc)

@return_execution_time
def time_bubble_sort(sample: List):
    bubble_sort(sample)

if __name__ == "__main__":
    bubble_sort(List(42))
    bubble_sort(random_list(5))


