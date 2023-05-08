from typing import Self

class Node:
    def __init__(self, value, next: Self or None =None):
        """# {{{
        Tests:
        >>> A = Node(1, Node(2, Node('a', Node('b'))))
        >>> A.value
        1
        >>> A.next.value
        2
        >>> A.next.next.value
        'a'
        >>> A.next.next.next.value
        'b'
        >>> A.next.next.next.next is None
        True
        """# }}}
        self.value = value
        self._next = next

    def __iter__(self):
        return NodeIterator(self)

    @property
    def next(self):
        """# {{{
        Tests:
        >>> A = Node(1, Node(2, Node(3)))
        >>> A.next.value
        2
        >>> A.next.next.value
        3
        >>> A.next.next.next is None
        True
        """# }}}
        return self._next

    @next.setter
    def next(self, val: Self or None) -> None:
        """# {{{
        Tests:
        >>> A = Node()
        >>> A.next = Node(1)
        >>> A.next = Node(3)
        >>> A.next.next = Node(1)
        >>> A.next.next.next = Node(4)
        >>> A.next.next.next.value
        4
        """# }}}
        if val is None:
            self._next = None
        elif isinstance(val, Node):
            self._next = val
        else:
            raise TypeError(f"next must be a Node or None, not {type(val)}.")


class NodeIterator:
    def __init__(self, node: Node):
        self.node = node

    def __iter__(self):
        """# {{{
        Tests:
        >>> A = Node(1, Node(2, Node(3, Node(4))))
        >>> list(A)
        [1, 2, 3, 4]
        >>> list(Node('test'))
        ['test']
        """# }}}
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration
        val = self.node.value
        self.node = self.node.next
        return val


if __name__ == '__main__':
    L = Node(3, Node(1, Node(4, Node(1, Node(5, Node(9, Node(2, Node(6))))))))
    print(list(L))



