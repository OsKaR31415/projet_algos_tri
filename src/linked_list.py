from __future__ import annotations
from node import Node, NodeIterator

class List:
    def __init__(self, *head: List or Node or None):
        """# {{{
        Args:
            No arguments : Create an empty List
            head (None): Create an empty list.
            head (Node): Create a List out of a linked Nodes.
            head (List): Does nothing to a list (not a copy).
            *head: Create a list from the list of arguments passed.
        Tests:
            >>> L = List(Node(1, Node(2, Node(3))))
            >>> L2 = List(L)
            >>> L.head is L2.head  # not a copy
            True
            >>> L.head.value
            1
            >>> L.head.next.value
            2
            >>> L.head.next.next.value
            3
            >>> L.head.next.next.next is None  # end of the list
            True
            >>> List().head is None  # empty list : head is None
            True
            >>> A = List(7, 8, 9, 10, 11)
            >>> A.head.value
            7
            >>> A.head.next.value
            8
            >>> A.head.next.next.value
            9
            >>> A.head.next.next.next.value
            10
            >>> A.head.next.next.next.next.value
            11
            >>> List(None)  # /!\ this declares an empty list
            List()"""# }}}

        match head:
            case ():  # empty tuple : no arguments given
                self._head = None
            case (None,):  # None should mean empty list
                # this is because, when you transform a node into a list, you
                # want None to represent the empty Node.
                self._head = None
            case (node,) if isinstance(node, Node):
                self._head = head[0]
            case (linked_list,) if isinstance(linked_list, List):
                # /!\ The structure is not copied
                self._head = linked_list.head
            case _:
                self.__init_from_iterable__(head)

    def __init_from_iterable__(self, iterable: iter) -> None:
        try:
            iterator = iter(iterable)
        except:
            raise TypeError(
                f"next must be of type Node or List or iterable, not {type(next)}.")
        self._head = Node(None)  # node with useless contents
        tail = self._head  # last node of self._head
        for element in iterable:
            tail.next = Node(element)
            tail = tail.next
        # remove the first element, None, that is useless
        self._head = self._head.next

    @property
    def head(self) -> Node or None:
        return self._head

    @head.setter
    def head(self, value: Node or None) -> None:
        if isinstance(value, Node) or value is None:
            self._head = value
        else:
            raise TypeError(
                f"head must be of type Node or None, not {type(value)}.")

    @property
    def next(self) -> Node or None:
        return List(self._head.next)

    @next.setter
    def next(self, value: Node or None) -> None:
        """Get the next List.
        That is the list of all the elements except the first.
        """
        if self.head is None:
            raise EmptyListError("Empty list has no next.")
        elif value is None:
            self._head.next = None
        elif isinstance(value, Node):
            self.head.next = value
        elif isinstance(value, List):
            self.head.next = value.head
        else:
            raise TypeError(
                f"next must be of type List, Node or None, not {type(value)}.")

    @next.deleter
    def next(self) -> None:
        """Deletes the next element(s) of the List.# {{{
        It makes the current node the last one of the List.
        """# }}}
        # must use __del__, else the attribute is deleted, but not its contents.
        self._head.__del__()
        self._head.next = None

    @property
    def value(self) -> object:
        """Get the value of the first node of this List."""
        if self.is_empty():
            raise EmptyListError("Empty list has no value.")
        return self._head.value

    @value.setter
    def value(self, new_value: All) -> None:
        """Change the value of the first node of this List."""
        if self.is_empty():
            raise EmptyListError("Empty list can't have any value.")
        self.head.value = new_value

    def __str__(self) -> str:
        """# {{{
        Tests:
            >>> print(List())
            < >
            >>> print(List(Node(None)))
            <None>
            >>> print(List(Node(1, Node(2))))
            <1, 2>
            >>> print(List(1, 2, 3, 'a', 'b', 'c'))
            <1, 2, 3, 'a', 'b', 'c'>
        """# }}}

        if self.is_empty():
            return "< >"
        return "<" + ", ".join(map(repr, list(self))) + ">"

    def __repr__(self) -> str:
        """# {{{
        Tests:
            >>> repr(List(1, 2, 3, 'a', 'b', 'c'))
            "List(1, 2, 3, 'a', 'b', 'c')"
        """# }}}

        if self.is_empty():
            return "List()"
        elements = list(map(repr, list(self)))
        return "List(" + ", ".join(elements) + ")"

    def __len__(self) -> int:
        """# {{{
        Tests:
            >>> len(List())
            0
            >>> len(List(Node(1)))
            1
            >>> len(List(Node(1, Node(2, Node(3)))))
            3
        """# }}}

        if self.is_empty():
            return 0
        length = 0
        p = self.head
        while p is not None:
            p = p.next
            length += 1
        return length

    def __iter__(self) -> NodeIterator:
        """
        Tests:
            >>> L = List(Node(1, Node(2, Node(3, Node('a', Node('b', Node('c')))))))
            >>> list(L)
            [1, 2, 3, 'a', 'b', 'c']
        """
        if self.is_empty():
            return iter([])
        return iter(self.head)

    def copy(self) -> List:
        """Return a copy of this List."""
        # Use the fact that Lists are iterable, and that they can be built from
        # a list of arguments
        return List(*self)

    def is_empty(self) -> bool:
        """# {{{
        Predicate checking if the list is empty.
        Tests:
            >>> List().is_empty()
            True
            >>> List(None).is_empty()  # List(None) really is an empty list.
            True
            >>> List(Node(42)).is_empty()
            False
            >>> List(Node(42, Node(73))).is_empty()
            False
        """# }}}
        return self.head is None

    def car(self) -> object:
        """First value of the list.# {{{
        Tests:
            >>> List(Node(42)).car()
            42
            >>> List(Node(42, Node(37, Node(28, Node(73))))).car()
            42
        """# }}}
        if self.is_empty():
            raise EmptyListError("Empty list has no first value.")
        return self._head.value

    def cdr(self) -> List:
        """List containing all but the first value of this list.# {{{
        Tests:
            >>> List().cdr()
            List()
            >>> List(Node(28)).cdr()
            List()
            >>> L = List(28, 37, 73, 42)
            >>> L.cdr()
            List(37, 73, 42)
            >>> L.cdr().cdr()
            List(73, 42)
            >>> L.cdr().cdr().cdr()
            List(42)
            >>> L.cdr().cdr().cdr().cdr()
            List()
        """# }}}
        if self.is_empty():
            return List()
        return List(self.head.next)

    def last(self) -> List:
        """Last Node of a linked list.# {{{
        Tests:
            >>> List().last().is_empty()
            True
            >>> List(28, 37, None, 42).last().value
            42
        """# }}}

        if self.is_empty():
            return List()
        p = self
        while not p.next.is_empty():
            p = p.next
        return p

    def delete_last(self) -> None:
        if self.is_empty():
            raise EmptyListError("Can't delete last node of an empty List")
        if self.next.is_empty():
            self._head = None
        p = self
        while not p.next.next.is_empty():
            p = p.next
        p.next = None


    def prepend(self, val: All) -> None:
        """Add a value at the beginning of the list.# {{{
        This modifies the list and returns nothing.
        Tests:
            >>> L = List()
            >>> L.prepend(42)
            >>> L
            List(42)
            >>> L.prepend(28); L.prepend(6)
            >>> L
            List(6, 28, 42)
            """# }}}
        self.head = Node(val, self.head)

    def append(self, val: All) -> None:
        """Add a value at the end of the list.# {{{
        This modifies the list and returns nothing.
        Tests:
            >>> L = List()
            >>> L.append(28)
            >>> L
            List(28)
            >>> L.append(42); L.append(6)
            >>> L
            List(28, 42, 6)
        """# }}}

        if self.head is None:
            self.head = Node(val)
        elif self.head.next is None:
            self.head.next = Node(val)
        else:
            self.cdr().append(val)


class EmptyListError(Exception):
    def __init__(self, message="Empty linked List."):
        self.message = message
        super().__init__(self.message)


if __name__ == "__main__":
    # L = List()
    # for v in [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]:
    #     L.append(v)
    # print(L)
    # L.prepend(3)
    # print(L)
    # print(L.last().value)

    L = List(3, 1, 4, 1, 5, 9, 2)
    del L.next.head
    print(L)
