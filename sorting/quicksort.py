def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,l,h):
	i = ( l - 1 )
	x = arr[h]

	for j in range(l , h):
		if arr[j] <= x:

			# increment index of smaller element
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[h] = arr[h],arr[i+1]
	return (i+1)

# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quickSortIterative(arr,l,h):

	# Create an auxiliary stack
	size = h - l + 1
	stack = [0] * (size)

	# initialize top of stack
	top = -1

	# push initial values of l and h to stack
	top = top + 1
	stack[top] = l
	top = top + 1
	stack[top] = h

	# Keep popping from stack while is not empty
	while top >= 0:

		# Pop h and l
		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1

		# Set pivot element at its correct position in
		# sorted array
		p = partition( arr, l, h )

		# If there are elements on left side of pivot,
		# then push left side to stack
		if p-1 > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = p - 1

		# If there are elements on right side of pivot,
		# then push right side to stack
		if p+1 < h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h 

# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
	print ("%d" %arr[i]),

# This code is contributed by Mohit Kumra
