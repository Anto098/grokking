'''
Problem Statement
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, seq):
    if len(seq) == 0:
        return True

    elif root is None:
        return False

    if root.val == seq[0]:
        return find_path(root.left, seq[1:]) or find_path(root.right, seq[1:])
    else:
        return False





def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
