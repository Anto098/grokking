from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


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

def traverse_v2(root):
    result = [[root.val]]
    current_level = [root]
    while current_level:
        for elem in current_level:
            next_level = []
            next_level.extend([n for n in [elem.left, elem.right] if n])

        if next_level:
            result.append([elem.val for elem in next_level])
        current_level = next_level

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Level order traversal: {traverse(root)}")
    print(f"Level order traversal: {traverse_v2(root)}")
