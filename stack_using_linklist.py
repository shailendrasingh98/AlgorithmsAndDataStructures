# Implement stack using link list
from linked_list import LinkedList


class Stack(object):
    """Stack implementaion using linked list """
    def __init__(self, size = None):
        self.ll = LinkedList()
        self.size = size
        self.count = 0

    def push(self, data):
        if self.isFull():
            print("Stack is Full")
            return

        self.ll.add(data)
        self.count +=1
        print("Pushed...")

    def pop(self):
        if self.isEmpty():return

        top = self.ll.head
        self.ll.head = top.next
        data = top.data
        top.next = None
        del(top)
        self.count -=1
        return data

    def peek(self):
        if self.isEmpty():return
        top = self.ll.head
        return top.data

    def isEmpty(self):
        if self.count <=0:
            return True
        return False

    def isFull(self):
        if not self.size:
            print("there is no limit of stack, it won't overflow until system's stack overflows")
            return False
        if self.count >= self.size:
            return True
        return False
