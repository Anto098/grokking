class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    # paths = []
    # use an array so the value is kept during recursion
    paths = [0]
    _count_paths(root, S, [], paths)

    # return len(paths)
    return paths[0]


def _count_paths(root, S, path, paths):
    if root is None:
        return 0
    path.insert(0, root.val)
    if not root.left and not root.right:
        s = 0
        for i in range(len(path)):
            s += path[i]
            if s == S:
                # paths.append(path[:i + 1])
                paths[0] += 1
            elif s > S:
                break
    else:
        _count_paths(root.left, S, path, paths)
        _count_paths(root.right, S, path, paths)

    path.pop(0)


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Tree has paths: {count_paths(root, 11)}")
