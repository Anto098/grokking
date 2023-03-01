from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(f"{current.val} ", end='')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    prev = [root]
    while prev:
        temp = []
        for node in prev:
            temp.extend([n for n in [node.left, node.right] if n])

        n = len(temp)
        if n > 0:
            for i in range(n-1):
                temp[i].next = temp[i + 1]
            else:
                temp[-1].next = None

        prev = temp

    return root


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()
