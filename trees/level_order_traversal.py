# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A recursive process to print level order traveral of BT
def levelOrderTraversal(root):
    #list as queue
    queue = []
    # Base CAse
    if root is None:
        return
    # push root to queue
    queue.append(root)
    #while queue beocmes empty
    while len(queue) > 0:
        curr = queue.pop(0)           # pop first data
        print(curr.data , end = ' ') # print data
        #insert left and right children of current to queue
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

# print node without siblings in tree
def nodesWithoutSiblings(root):
    if not root:
        return

    if root.left and not root.right:
         print(root.left.data )
    if not root.left and root.right:
        print(root.right.data)
    nodesWithoutSiblings(root.left)
    nodesWithoutSiblings(root.right)

def pathsToLeaves(root, paths):
    # base case
    if not root:
        return
    paths.append(root.data)
    if not root.left and not root.right:
        print(*paths)

    pathsToLeaves(root.left, paths)
    pathsToLeaves(root.right, paths)
    paths.pop()

def minDepthOfTree(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    left = minDepthOfTree(root.left) if root.left else float('inf')
    right = minDepthOfTree(root.right) if root.right else float('inf')
    return 1 + min(left, right)

def maxDepthOfTree(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    left = maxDepthOfTree(root.left) if root.left else float('-inf')
    right = maxDepthOfTree(root.right) if root.right else float('-inf')
    return 1 + max(left, right)

def sumOfleftLeaves(root, left, l, r):
    # base case
    if not root:
        return 0
    if not root.left and not root.right and left:
        return root.data

    l+=sumOfleftLeaves(root.left, True, l, r)
    r+=sumOfleftLeaves(root.right, False, l,r)
    return max(l,r)

def sumOfRightLeaves(root, right, l, r):
    # base case
    if not root:
        return 0
    if not root.left and not root.right and right:
        return root.data
    r+=sumOfRightLeaves(root.right, True, l,r)
    l+=sumOfRightLeaves(root.left, False, l, r)
    return max(l,r)

def deepestOddLevelLeaf(root, level):
    # base case
    if not root:
        return 0
    # check if level changed and print first element
    if level % 2 != 0 and not root.left and not root.right:
        return level

    #recursively call right sub tree then left sub tree
    return max(deepestOddLevelLeaf(root.right, level+1)
    ,deepestOddLevelLeaf(root.left, level+1))

def isFullBinaryTree(root):
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue)>0:
        curr = queue.pop(0)
        if curr.left and not curr.right:
            return False
        if not curr.left and curr.right:
            return False
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return True

def isCompleteBinaryTree(root):
    if not root:
        return True
    queue = []
    non_full_node_seen = False
    queue.append(root)
    while len(queue)>0:
        curr = queue.pop(0)
        if curr.left and curr.right:
            if non_full_node_seen:
                return False
            non_full_node_seen = True
            queue.append(root.left)
            queue.append(root.left)
        if curr.left and not curr.right:
            if non_full_node_seen:
                return False
            non_full_node_seen = True
            queue.append(root.left)
        if not curr.left and curr.right:
            return False
    return True

def countLeaves(root):
    # count leaves of Tree
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    return countLeaves(root.left) + countLeaves(root.left)

def isIdentical(root1, root2):
    if root1 and not root2:
        return False
    if not root1 and root2:
        return False
    if not root1 and not root2:
        return True
    if root1.data !=root2.data:
        return False
    return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)


def max_height(root):
    if root is None: return 0
    if root.left is None and root.right is None: return 1
    return max(max_height(root.left), max_height(root.right)) +1

def diameter(root):
    if root is None: return 0
    mx_height = 1 + max(maxDepthOfTree(root.left), maxDepthOfTree(root.right))
    return max(max(diameter(root.left),diameter(root.right)), mx_height)

# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
root.right.right = Node(6)
print('========Level order traversal========' )
levelOrderTraversal(root)
print()
print('========Node without siblings========' )
nodesWithoutSiblings(root)
print()
print('========paths from root to leaves=====')
pathsToLeaves(root, [])
print()
print('========Min Depth of Tree===========' )
print(minDepthOfTree(root))
print()
print('========Max Depth of Tree===========' )
print(maxDepthOfTree(root))
print()
print('========sum of left leaves of Tree===========' )
print(sumOfleftLeaves(root,False,0,0))
print()
print('========sum of right leaves of Tree===========' )
print(sumOfRightLeaves(root,False,0,0))
print()
print('=====depth of deepest odd level Leaf ==========')
print(deepestOddLevelLeaf(root, 1))
print('============is Full binary Tree ==============')
print(isFullBinaryTree(root))
print('============is Complete binary Tree ==============')
print(isCompleteBinaryTree(root))
