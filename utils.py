from linked_list import List
from random import randint

def iota(n: int) -> List:
    """
    Tests:
        >>> iota(0)
        List()
        >>> iota(1)
        List(Node(1))
        >>> iota(5)
        List(Node(1, Node(2, Node(3, Node(4, Node(5))))))
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


def random_list(length: int):
    new_list = List()
    for _ in range(length):
        new_list.prepend(randint(1, 100))
    return new_list




