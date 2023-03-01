class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    paths = []
    _find_sum_of_path_numbers(root, [], paths)
    return sum(paths)


def _find_sum_of_path_numbers(root, path, paths):
    pass


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    s = 23
    print(f"Tree paths with sum {s}: {find_sum_of_path_numbers(root)}")
