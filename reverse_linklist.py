
from linked_list import LinkedList

class reverseLinkedList(LinkedList):
    """class to reverse linked list using itrative and recursive way"""

    def reverseList(self):
        # Code here
        temp = None
        if self.head is None:
            return None
        while self.head.next:
            prev = self.head
            nxt = self.head.next
            self.head.next = temp
            #prev.next = self.head.next
            self.head = nxt
            temp = prev

        self.head.next = temp

    def recursiveReverse(self):
        # head is None, no linked_list
        if self.head is None:
            return

        prev = self.head
        # if only one element in linklist
        if prev.next is None:
            return
        # increase head pointer
        self.head = prev.next
        self.recursiveReverse()
        #link next link of nextnode of prev node to prev node
        prev.next.next = prev
        #make prev node's next link to point to None
        prev.next = None


if __name__ == '__main__':
    print('Driver utility...')
    ll = reverseLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    print('linklist.....before reversing ')
    ll.show()
    ll.reverseList()
    print('linklist.....after reversing')
    ll.show()

    print('linklist.....before recusive reversing ')
    ll.show()
    ll.recursiveReverse()
    print('linklist.....after recusive reversing')
    ll.show()
