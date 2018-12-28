
# A simple Python program to introduce a linked list

class Node(object):
    '''Node class:
    @Input: Data - data to be store in node
    input : next - refrence to next, default is None
     '''
    def __init__(self, data, nextNode = None):
        self.data = data
        self.next = nextNode

    #Node features to set and get data and next node
    def getdata(self):
       return self.data

    def setdata(self,val):
       self.data = val

    def getnextNode(self):
       return self.next

    def setnextNode(self,val):
       self.next = val

class LinkedList(object):
    """"Link list class
    """
    def __init__(self):
        self.head = None
        self.size  = 0

    def add(self, data):
        """
        To add data in link list
        @Args: data to be store
        """
        print('Adding a node in link list...')
        newNode      = Node(data)
        newNode.next =self.head
        self.head    = newNode
        self.size+=1
        return True

    def insertAt(self, data, ind):
        """
        To insert a node at given index in link list
        @Args: data to be store and index
        """
        if not self.size or not ind:
            self.add(data)
            return
        newNode = Node(data)
        temp = self.head
        while ind-1:
            if not temp.next:
                raise IndexError('index ({!r}) is not in link list'.format(ind))
                break
            temp = temp.next
            ind-=1
        next = temp.next
        temp.next = newNode
        newNode.next = next
        self.size+=1

    def show(self):
        """ Prints link list
        """
        temp = self.head
        while temp:
            print('{!r} => '.format(temp.data), end = '')
            temp = temp.next
        print('None')

    def size(self):
        ''' Size of link list '''
        return self.size

    def isEmpty(self):
        '''True if link list has no node'''
        return not bool(self.size)

    def delet(self, data):
        '''delets first occurance of data from link LinkedList
        @Args: data - to be deleted from link list'''
        if self.isEmpty():
            print('Link list is empty')
            return
        temp = self.head
        if self.size==1 and temp.data==data:
            print('Only one data entry in liked list...deleting entry...')
            temp.next =None
            self.head = None
            del(temp)
            self.size-=1
            return
        prev = self.head
        next = temp.next
        while prev.next:
            temp = prev.next
            next = temp.next
            if data == temp.data:
                print('Deleting...')
                temp.next = None
                prev.next = None
                del(temp)
                self.size-=1
                break
            prev = temp
        prev.next = next
