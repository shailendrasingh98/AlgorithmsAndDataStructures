class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

class BinarySearchTree(object):
    """docstring for BinarySearchTree."""

    def __init__(self, _data):
        self.root = Node(_data)

    def insert(self, root, data):
        # If the tree is empty, return a new node
        if root is None:
            return Node(data)

        # Otherwise recur down the tree
        if data < root._data:
            root._left = self.insert(root._left, data)
        else:
            root._right = self.insert(root._right, data)

        # return the (unchanged) node pointer
        return root


    def InOrderTraversal(self, root):
        if root:
            self.InOrderTraversal(root._left)
            print(root._data, end = ' ')
            self.InOrderTraversal(root._right)

    def minValueNode(self, root):
        current = root
        # loop down to find the leftmost leaf
        while(current._left is not None):
            current = current._left
        return current._data

    def deleteNode(self, root, data):
        # Base Case
        if root is None:
            return root
        # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if data < root._data:
            root._left = self.deleteNode(root._left, data)
        # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif(data > root._data):
            root._right = self.deleteNode(root._right, data)
        # If key is same as root's key, then this is the node
        # to be deleted
        else:
            # Node with only one child or no child
            if root._left is None :
                temp = root._right
                root = None
                return temp
            elif root._right is None :
                temp = root._left
                root = None
                return temp
            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root._right)
            # Copy the inorder successor's content to this node
            root.data = temp
            # Delete the inorder successor
            root._right = self.deleteNode(root._right , temp)
        return root

    def search(self, root, data):
        # Base Cases: root is null or key is present at root
        if root is None or root._data == data:
            return root

        # Key is greater than root's key
        if root._data < data:
            return search(root._right, data)

        # Key is smaller than root's key
        return search(root._left, data)

if __name__ == '__main__':
    b = BinarySearchTree(13)
    b.root = b.insert(b.root, 10)
    b.root = b.insert(b.root, 14)
    b.root = b.insert(b.root, 15)
    b.root = b.insert(b.root, 8)
    b.root = b.insert(b.root, 9)
    b.root = b.insert(b.root, 7)
    b.root = b.insert(b.root, 11)
    b.root = b.insert(b.root, 6)
    b.root = b.insert(b.root, 16)
    b.root = b.insert(b.root, 17)
    b.root = b.insert(b.root, 18)
    b.root = b.insert(b.root, 19)
    b.InOrderTraversal(b.root)
    print()
    print('minimum:%d' %b.minValueNode(b.root))
    b.deleteNode(b.root, 15)
    b.InOrderTraversal(b.root)
