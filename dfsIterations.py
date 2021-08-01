class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


def inorderTraversal(root):
    res = []
    stack = []
    while stack or root:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.value)
            root = node.right
    return res


def postorderTraversal(root):
    stack, res = [], []
    while stack or root:
        if root:
            stack.append(root)
            res.append(root.value)
            root = root.right
        else:
            node = stack.pop()
            root = node.left
    return res[::-1]


head = TreeNode(1)
currentNode = head
currentNode.left = TreeNode(2)
currentNode.right = TreeNode(3)
currentNode = currentNode.left
currentNode.left = TreeNode(4)
currentNode.right = TreeNode(5)

print(preorderTraversal(head))
print(inorderTraversal(head))
print(postorderTraversal(head))
