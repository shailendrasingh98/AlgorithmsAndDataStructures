import math

class Search(object):
    def recursiveBinarySearch(self, data, lst, start, end):
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


    def binarySearch(self, data, lst):
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
                return mid
            # Or does the target precede the midpoint?
            elif data < lst[mid]:
                high = mid-1
            else:
            # Or does it follow the midpoint?
                low = mid+1

        # If the sequence cannot be subdivided further, we're done.
        return -1

    def findSortedPosition(self, data, lst):
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

    def jumpSearch(self, arr, x):
        n = len(arr)
        #calculate step size to jump
        step = int(math.sqrt(n))
        prev = next = 0
        # Find block where data resides
        for i in range(0, n, step):
            if arr[i] == x:
                return i
            if arr[i]>x:
                next = i
                break
        #prev index
        prev = next - step
        # lenear search in block
        for i in range(prev, min(next+1,n)):
            if arr[i] ==x:
                return i


    def interpolationSearch(self, arr, x):
        lo = 0
        hi = len(arr)-1

        while lo <= hi and x <=arr[hi] and x >=arr[lo]:
            if lo == hi:
                if x ==arr[lo]:
                    return lo
                return -1
            # find position to search
            pos = lo + int(((hi - lo)/(arr[hi]-arr[lo]))*(x - arr[lo]))

            if arr[pos] == x:
                return pos
            elif arr[pos] < x:
                lo = pos +1
            else:
                hi = pos -1
        return -1

    def binarySearch2(self, arr, l, r, x):
        if r >= l:
            mid = int(l + ( r-l ) // 2)

            # If the element is present at
            # the middle itself
            if arr[mid] == x:
                return mid

            # If the element is smaller than mid,
            # then it can only be present in the
            # left subarray
            if arr[mid] > x:
                return self.binarySearch2(arr, l,
                                    mid - 1, x)

            # Else he element can only be
            # present in the right
            return self.binarySearch2(arr, mid + 1, r, x)

        # We reach here if the element is not present
        return -1

    def exponentialSearch(self, arr, x):
        n = len(arr)
        # IF x is present at first location itself
        if arr[0] == x:
            return 0
        i =1
        # Find range for binary search j by repeated doubling
        while i < n and arr[i] <= x:
            i = i * 2

        # Call binary search for the found range
        print(i//2, i)
        return self.binarySearch2( arr, i / 2,
                         min(i, n), x)


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
    #print(binarySearch(12, l))       #True
    #print(binarySearch(99, l))       #False
    print(jumpSearch(l, 12))
    print(interpolationSearch(l, 12))
    print(exponentialSearch(l, 12))
