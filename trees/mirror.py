# create mirror of binary tree
# Complete function below which takes root as an argument

def mirror(root):
    base case
    if not root: return None
    #recursively call left and right sub tree
    mirror(root.left)
    mirror(root.right)
    # while at leaves, switch the leaves
    root.left, root.right = root.right, root.left
