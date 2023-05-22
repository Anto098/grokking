class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root is None or sum < 0:
        return False
    sum -= root.val
    if sum == 0 and not (root.left or root.right):
        return True
    return has_path(root.left, sum) or has_path(root.right, sum)


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(f"Tree has path: {has_path(root, 23)}")
    print(f"Tree has path: {has_path(root, 16)}")
