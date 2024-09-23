class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def SymmetricTree(strArr):
    def isMirror(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.val == node2.val) and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

    def buildTree(arr, index):
        if index >= len(arr) or arr[index] == '#':
            return None
        node = TreeNode(int(arr[index]))
        node.left = buildTree(arr, 2 * index + 1)
        node.right = buildTree(arr, 2 * index + 2)
        return node

    root = buildTree(strArr, 0)
    return isMirror(root, root)



StrArr = input("Enter space-separated elements: ").split()
print(StrArr)

print(SymmetricTree(StrArr))


#-------------------------------------------------End-------------------------------------------------#
