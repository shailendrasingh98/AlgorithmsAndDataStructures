# python implemetation of right view of tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Views:
    level_so_far = -1
    # A recursive approach to print right view of tree
    def rightViewOfTree(self,root, level):

        # base case
        if not root:
            return

        # check if level changed and print first element
        if level > self.level_so_far:
            self.level_so_far = level
            print(root.data, end = ' ')

        #recursively call right sub tree then left sub tree
        self.rightViewOfTree(root.right, level+1)
        self.rightViewOfTree(root.left, level+1)

    # A recursive approach to print left view of tree
    def leftViewOfTree(self,root, level):

        # base case
        if not root:
            return

        # check if level changed and print first element
        if level > self.level_so_far:
            self.level_so_far = level
            print(root.data, end = ' ')

        #recursively call right sub tree then left sub tree
        self.leftViewOfTree(root.left, level+1)
        self.leftViewOfTree(root.right, level+1)

if __name__ == '__main__':
    # Driver program to test above function
    v = Views()
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(4)
    root.right.left.rght = Node(6)
    root.right.left.left = Node(7)
    root.left.left.left = Node(9)
    root.left.left.left.left = Node(11)
    print('===============left view=======================')
    v.leftViewOfTree(root, 0)
    print()
    print('===============right view=======================')
    v.level_so_far = -1
    v.rightViewOfTree(root, 0)

# output
'''
===============left view=======================
10 8 3
===============right view=======================
10 2 2
'''
