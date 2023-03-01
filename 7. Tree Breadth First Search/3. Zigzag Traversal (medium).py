class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    prev = [root]
    left_to_right = False
    while prev != []:
        temp = []
        for node in prev[::-1]:
            # need to reverse the previous floor every time because they want us to zigzag (from LTR to RTL)
            nodes = [n for n in [node.left, node.right] if n]
            temp.extend(nodes) if left_to_right else temp.extend(nodes[::-1])
        result.append(prev)
        prev = temp
        left_to_right = not left_to_right
    return list(map(lambda l: [item.val for item in l], result))


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print(f"Level order traversal: {traverse(root)}")
