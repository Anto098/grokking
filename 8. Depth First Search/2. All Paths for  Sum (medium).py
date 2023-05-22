class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    return _find_paths(root, sum, path=[], paths=[])


def _find_paths(root, sum, path, paths):
    if root is None or sum < 0:
        return []
    path.append(root.val)
    sum -= root.val
    h = len(path)  # height that we're at in the tree
    if sum == 0 and not root.left and not root.right:
        paths.append(path)
        return paths
    # path[:h] because the elements added by the `_find_path` call on the left child will add to the path,
    # but we don't want to have it for the exploration of the right part of the tree
    # reset paths to an empty list otherwise we keep duplicates
    return _find_paths(root.left, sum, path, paths=[]) + _find_paths(root.right, sum, path[:h], paths=[])


def find_paths_v2(root, sum):
    all_paths = []
    find_paths_recursive(root, sum, paths=all_paths, path=[])
    return all_paths


def find_paths_recursive(root, sum, paths, path):
    # instead of returning the result, we save it in a variable that's created outside the function
    # saves us all the problems from saving results correctly
    if root is None:
        return
    sum -= root.val
    path.append(root.val)
    if sum == 0 and not (root.left or root.right):
        paths.append(path.copy())
    else:
        find_paths_recursive(root.left, sum, paths, path)
        find_paths_recursive(root.right, sum, paths, path)

    path.pop(-1)


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print(f"Tree paths with sum {sum}: {find_paths(root, sum)}")
    print(f"Tree paths with sum {sum}: {find_paths_v2(root, sum)}")
