from linked_list import LinkedList

#Find nth node from the end of a Linked List.
# Added two methods to find nth node from last of linked list

def find_nthNodeFromLast(linklist, k):
    # find nth node of linked list from last using hashing
    temp = linklist.head
    nodeMap = dict()
    i=1
    while temp !=None:
        nodeMap[i]=temp.data
        temp = temp.next
        i+=1
    print(nodeMap[i-k])

def find_nthNodeFromLastUsing2Pointers(linklist, k):
    # find nth node of linked list from last using 2 pointers
    #Best method
    first = last = linklist.head
    i=1
    while first.next !=None:
        if i >= k:
            #start second ponter only when first poiter traverse k steps
            #maintain last - first pointer position == k
            last = last.next
        first = first.next
        i+=1
    print(last.data)

if __name__ == '__main__':
    print('Driver utility...')
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.show()
    find_nthNodeFromLast(ll, 4)
    find_nthNodeFromLastUsing2Pointers(ll, 4)
