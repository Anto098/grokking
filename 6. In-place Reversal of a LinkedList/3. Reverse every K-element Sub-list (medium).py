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


def reverse_every_k_elements(head, k):
    dragging, mid = None, head
    while mid is not None:
        outer_beginning = dragging
        inner_beginning = mid
        i = 1

        while i < k + 1 and mid is not None:
            ahead = mid.next
            mid.next = dragging
            dragging = mid
            mid = ahead
            i += 1

        inner_ending = dragging
        outer_ending = mid
        inner_beginning.next = outer_ending
        if outer_beginning is None:
            # first iteration
            head = inner_ending
        else:
            outer_beginning.next = inner_ending

        dragging = inner_beginning  # inner beginning, which is now right before mid

    return head


if __name__ == "__main__":
    outer_head = Node(1)
    outer_head.next = Node(2)
    outer_head.next.next = Node(3)
    outer_head.next.next.next = Node(4)
    outer_head.next.next.next.next = Node(5)
    outer_head.next.next.next.next.next = Node(6)
    outer_head.next.next.next.next.next.next = Node(7)
    outer_head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end="")
    outer_head.print_list()
    result = reverse_every_k_elements(outer_head, 3)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()
