array = [1, 2, 3, 4, 5, 6, 7, 8]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def builder(start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = TreeNode(array[mid])
    node.left = builder(start, mid - 1)
    node.right = builder(mid + 1, end)
    return node


def preorderTraversal(root):
    stack, res = [], []
    while stack or root:
        if root is not None:
            stack.append(root)
            res.append(root.value)
            root = root.left
        else:
            node = stack.pop()

            root = node.right
    return res


print(preorderTraversal(builder(0, len(array) - 1)))
