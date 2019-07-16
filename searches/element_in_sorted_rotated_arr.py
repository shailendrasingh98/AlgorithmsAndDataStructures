# Given a sorted and rotated array A of N distinct elements which is rotated at some point,
# and given an element K. The task is to find the index of the given element K in the array A.

def binarySearch(arr, x):
    s = 0
    e = len(arr)-1
    while s <=e:
        m = (s+e)//2

        if arr[m] ==x:
            return m
        # mid lies in left line
        elif arr[s] <= arr[m]:
            if arr[s] <= x <= arr[m]:
                e = m-1
            else:
                s = m+1
        # mis lies in right line
        elif arr[m] <=x and x<=arr[e]:
            s = m +1
        else:
            e = m-1
    return -1
