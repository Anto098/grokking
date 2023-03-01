from __future__ import print_function


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_middle_of_linked_list(head):
    s, f = head, head
    while True:
        s = s.next
        f = f.next.next
        if f is None or f.next is None:
            return s


if __name__ == "__main__":
    _head = Node(1)
    _head.next = Node(2)
    _head.next.next = Node(3)
    _head.next.next.next = Node(4)
    _head.next.next.next.next = Node(5)

    print(find_middle_of_linked_list(_head).value)

    _head.next.next.next.next.next = Node(6)
    print(find_middle_of_linked_list(_head).value)

    _head.next.next.next.next.next.next = Node(7)
    print(find_middle_of_linked_list(_head).value)
