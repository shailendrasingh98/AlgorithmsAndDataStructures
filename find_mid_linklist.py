from linked_list import LinkedList
# we can middle efficiently by starting two pointer
# slow - which walks one step
# fast - which walks two step
# by the time fast will reach to end of ll,
# slow pointer must have reached to middle.
def findMiddle(head):
    # initialize both to head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next      # one step
        fast = fast.next.next # two steps
    return slow               # middle


if __name__ == '__main__':
    print('Driver utility...')
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    print('linklist.....')
    ll.show()
    mid = findMiddle(ll.head)
    print('mid element in above link list')
    print(mid.data)
