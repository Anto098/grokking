class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    paths = []
    _find_sum_of_path_numbers(root, [], paths)
    return sum([int(''.join([str(n) for n in nums])) for nums in paths])


def _find_sum_of_path_numbers(root, path, paths):
    if root is None:
        return

    path.append(root.val)
    if not root.left and not root.right:
        paths.append(path.copy())
    else:
        _find_sum_of_path_numbers(root.left, path, paths)
        _find_sum_of_path_numbers(root.right, path, paths)

    path.pop(-1)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print(f"Total sum of path numbers: {find_sum_of_path_numbers(root)}")
