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


def find_cycle_length(head):
    # step 1: find the cycle
    n1 = head.next
    n2 = head.next.next
    while n1 != n2:
        if n2 is not None and n2.next is not None:
            n1 = n1.next
            n2 = n2.next.next
        else:
            return False

    # step 2: find its length
    cycle_length = 0
    while True:
        n1 = n1.next
        cycle_length += 1
        if n1 == n2:
            break

    return cycle_length


def find_cycle_start(head):
    p1 = head
    p2 = head

    cycle_length = find_cycle_length(head)

    for i in range(cycle_length):
        p2 = p2.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


if __name__ == "__main__":
    _head = Node(1)
    _head.next = Node(2)
    _head.next.next = Node(3)
    _head.next.next.next = Node(4)
    _head.next.next.next.next = Node(5)
    _head.next.next.next.next.next = Node(6)

    _head.next.next.next.next.next = _head.next.next
    print(find_cycle_start(_head).value)

    _head.next.next.next.next.next = _head.next.next.next
    print(find_cycle_start(_head).value)

    _head.next.next.next.next.next = _head
    print(find_cycle_start(_head).value)
