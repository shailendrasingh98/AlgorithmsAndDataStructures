
def bubbleSort(lst):
# Sorts a sequence in ascending order using the bubble sort algorithm.
    for i in range(len(lst)-1):
        # Perform n-1 bubble operations on the sequence
        for j in range(len(lst)-i-1):
            # Bubble the largest item to the end.
            if lst[j] > lst[j+1]:
                # swap the j and j+1 items.
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def bubbleSortImproved(lst):
    # flag to determine to, if elements swapped
    swapped = True
    for i in range(len(lst)-1):
        if swapped:
            swapped = False
            for j in range(len(lst)-i-1):
                # check each pair and swap them if are not already in orde.r
                # Bubble the largest item to the end.
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    swapped = True
    return lst

def bubble_sort(listt):
    for i in range(len(listt)-1):
        if listt[i+1] < listt[i]:
            listt[i], listt[i+1] = listt[i+1], listt[i]
            bubble_sort(listt)
    return listt

def selectionSort(lst):
# Sorts a sequence in ascending order using the selection sort algorithm.
    for i in range(len(lst)):
        # Assume the ith element is the min.
        min = i
        # Determine if any other element contains a smaller value.
        for j in range(i, len(lst)):
            if lst[j]< lst[min]:
                min = j
        # Swap the ith value and min value only if the min value is
        # not already in its proper position
        if min !=i:
            lst[i], lst[min] = lst[min], lst[i]
    return lst

def insertionSort(lst):
    # Sorts a sequence in ascending order using the insertion sort algorithm.
    for i in range(len(lst)-1):
        # Starts with the first item as the only sorted entry.
        next = lst[i+1]
        for j in range(i+1, 0):
        # Find the position where value fits in the ordered part of the list.
        # Shift the items to the right during the search.
            if next < lst[j]:
                lst[j] = lst[j-1]
            # Put the saved value into the open slot.
            lst[j] = next

    return lst

def recursiveInsertion(lst, n):
    if n<=1:
        return
    recursiveInsertion(lst, n-1)
    last = lst[n-1]
    j = n-1
    while j>=0 and lst[j-1] > last:
        lst[j] = lst[j-1]
        j-=1
    lst[j-1] = last


if __name__ == '__main__':
    l = [1, 0, 123, 34, 54, 98, 45, 23, 2, 4, 9, 40, 54, 87, 78, 5,100]
    print("\nUnsorted list")
    print(l)

    print("Sorted list")
    # Bubble sort
    print(bubbleSort(l))
    print(bubbleSortImproved(l))
    # Selection sort
    print(selectionSort(l))

    # Insertion sort
    print(insertionSort(l))
