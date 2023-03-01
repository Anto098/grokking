class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    l = []
    prev = [root]
    while prev:
        temp = []
        for node in prev:
            temp.extend([n for n in [node.left, node.right] if n])

        l.extend(prev)
        prev = temp

    l = list(map(lambda x: x.val, l))
    n = len(l)
    for i, elem in enumerate(l):
        if elem == key and i+1 < n:
            return l[i + 1]
    return None


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 12)
    if result:
        print(result)
    result = find_successor(root, 9)
    if result:
        print(result)
