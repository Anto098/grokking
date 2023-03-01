class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0
    prev = [root]
    curr_depth = 0
    while prev:
        temp = []
        for node in prev:
            temp.extend([n for n in [node.left, node.right] if n])
        if len(temp) == 0:
            return curr_depth
        prev = temp
        curr_depth += 1


if __name__ == "__main__":
    outer_root = TreeNode(12)
    outer_root.left = TreeNode(7)
    outer_root.right = TreeNode(1)
    outer_root.right.left = TreeNode(10)
    outer_root.right.right = TreeNode(5)
    print(f"Tree Minimum Depth: {find_minimum_depth(outer_root)}")
    outer_root.left.left = TreeNode(9)
    outer_root.right.left.left = TreeNode(11)
    print(f"Tree Minimum Depth: {find_minimum_depth(outer_root)}")
