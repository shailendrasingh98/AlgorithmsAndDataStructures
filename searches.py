

def recursiveBinarySearch(data, lst, start, end):
    '''
    Binary search algorithm to search data in sorted list of data.

    :param input data: key/data to be search in List.
    :param input lst: collection of data in form of sorted list.
    :param start, end: starting and ending point of search.
    :return True: if data found in collection else False
    '''
    #if list is empty
    if not lst:
        return False

    # get the mid of list
    mid = (start+end)//2

    #base condition for recursion
    if start>=end:
        return False

    if lst[mid] == data:
    # data found, return True
        return True
    elif data < lst[mid]:
    # if data is less than the middle element
    # search in left half
        return binarySearch(data, lst, start, mid)
    else:
    # if data is greater than the middle element
    # search in right half
        return binarySearch(data, lst, mid+1, end)


def binarySearch(data, lst):
    '''
    Binary search algorithm to search data in sorted list of data.

    :param input data: key/data to be search in List
    :param input lst: collection of data in form of sorted list.
    :return True: if data found in collection else False
    '''
    # Start with the entire sequence of elements.
    low = 0
    high = len(lst)-1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (low+high)//2
        # Does the midpoint contain the target?
        if lst[mid] == data:
            return True
        # Or does the target precede the midpoint?
        elif data < lst[mid]:
            high = mid-1
        else:
        # Or does it follow the midpoint?
            low = mid+1

    # If the sequence cannot be subdivided further, we're done.
    return False

def findSortedPosition(data, lst):
    '''
    Modified version of the binary search that returns the index within
    a sorted sequence indicating where the target should be located.

    :param input data: key/data to be search in List.
    :param input lst: collection of data in form of sorted list.
    :return index: position of data in sorted list.
    '''
    # Start with the entire sequence of elements.
    low = 0
    high = len(lst)-1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (low+high)//2
        # Does the midpoint contain the target?
        if lst[mid] == data:
        # Index of the target
            return mid
        # Or does the target precede the midpoint?
        elif data < lst[mid]:
            high = mid-1
        else:
        # Or does it follow the midpoint?
            low = mid+1

    # Index where the target value should be.
    return low


if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 12, 34, 45, 100, 101, 102, 234, 456, 1000]
    # uncomment to search in recursion
    #print(recursiveBinarySearch(12, l, 0, len(l)))       #True
    #print(recursiveBinarySearch(99, l, 0, len(l)))       #False
    #print(recursiveBinarySearch(1, l, 0, len(l)))        #True
    #print(recursiveBinarySearch(1000, l, 0, len(l)))     #True
    #print(recursiveBinarySearch(1001, l, 0, len(l)))     #False
    #print(recursiveBinarySearch(0, l, 0, len(l)))        #False
    #print(recursiveBinarySearch(45, l, 0, len(l)))       #True
    #print(recursiveBinarySearch(7, l, 0, len(l)))        #True
    #print(recursiveBinarySearch(9, l, 0, len(l)))        #True

    # itrative method
    print(binarySearch(12, l))       #True
    print(binarySearch(99, l))       #False
