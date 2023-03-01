from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    d_idx, m_idx = 0, 1
    dragging, mid = None, head
    while m_idx < p:
        dragging, d_idx = mid, d_idx + 1
        mid, m_idx = mid.next, m_idx + 1
    outer_beginning = dragging
    inner_beginning = mid
    while m_idx < q + 1 and mid is not None:
        ahead = mid.next
        mid.next = dragging
        dragging, d_idx = mid, d_idx + 1
        mid, m_idx = ahead, m_idx + 1
    inner_ending = dragging
    outer_ending = mid
    outer_beginning.next = inner_ending
    inner_beginning.next = outer_ending

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()
