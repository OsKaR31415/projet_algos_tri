from linked_list import List
from utils import *


def bucket_sort(lst: List, max_value: int =None):
    """# {{{
    Args:
        lst (List): The list to sort. Must be a list of positive integers.
        max_value (int): The maximum integer in lst. It will be detected
            automatically if not specified.
    Tests:
        >>> all(is_sorted(bucket_sort(random_list(n))) for n in range(50))
        True
    """# }}}
    if lst.is_empty():
        return List()
    # find `max_value` : the maximum of the list
    if max_value is None:
        max_value = lst.value
        for elt in lst.cdr():
            if elt > max_value:
                max_value = elt
            if elt < 0:
                raise ValueError("Negative values not supported.")
    # initialize the list of buckets (list of zeroes)
    bucket = List()
    for _ in range(max_value+1):
        bucket.prepend(0)
    # loop over the elements
    for elt in lst:
        if elt > max_value:
            raise ValueError("value not in the bounds of the bucket.")
        current_bucket = bucket
        for _ in range(elt):
            current_bucket = current_bucket.next
        current_bucket.value += 1
    sorted_lst = List(True)  # list with a foo element
    sorted_lst_tail = sorted_lst
    for value, count in enumerate(bucket):
        for _ in range(count):
            sorted_lst_tail.next = List(value)
            sorted_lst_tail = sorted_lst_tail.next
    sorted_lst = sorted_lst.next  # remove the foo element
    return sorted_lst

@return_execution_time
def time_bucket_sort(sample: List, max_value: int =100):
    bucket_sort(sample, max_value)

if __name__ == "__main__":
    L = random_list(1000000)
    print(time_bucket_sort(L))



