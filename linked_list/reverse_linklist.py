
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
# This function should rotate list counter-
# clockwise by k and return new head (if changed)
def rotateList(self, head, k):
    # code here
    temp = newHead = head
    q = []
    l = 1
    n = k
    while temp.next:
        if k >=1:
            q.append(temp)
            newHead = temp.next
        temp = temp.next
        k = k-1
        l = l+1

    if n>=l:
        return head

    for node in q:
        temp.next = node
        temp = temp.next

    temp.next = None
    return newHead

def reverse_kth(self,head k):
    '''reverse a linked list in group of k'''
    prev = nxt = None
    c = k
    if head is None:
        return None
    if head.next is None:
        return head
    temp = head

    while temp and c :
        nxt = temp.next
        temp.next = prev
        prev = temp
        temp = nxt
        c -=1
    if nxt is not None:
        head.next = reverse(nxt, k)

    return prev


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
    ll.
    print('linklist.....after recusive reversing')
    ll.show()
