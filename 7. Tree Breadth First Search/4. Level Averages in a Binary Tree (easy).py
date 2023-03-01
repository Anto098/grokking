class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    return [sum(l) / len(l) for l in traverse(root)]


def traverse(root):
    result = []
    prev = [root]
    while prev != []:
        temp = []
        for node in prev:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        result.append(prev)
        prev = temp
    return list(map(lambda l: [item.val for item in l], result))


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Level averages are: {find_level_averages(root)}")
