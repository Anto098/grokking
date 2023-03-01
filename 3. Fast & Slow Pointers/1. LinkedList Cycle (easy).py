class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


def has_cycle(head):
    n1 = head.next
    n2 = head.next.next
    while n1 != n2:
        if n2 is not None and n2.next is not None:
            n1 = n1.next
            n2 = n2.next.next
        else:
            return False
    return True


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(has_cycle(head))

    head.next.next.next.next.next.next = head.next.next
    print(has_cycle(head))

    head.next.next.next.next.next.next = head.next.next.next
    print(has_cycle(head))
    print("😁 (press `ctrl + alt + ;` for the emojis menu, on pycharm) 😇")
