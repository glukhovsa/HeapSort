def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left<n and array[left]>array[largest]:
        largest = left

    if right<n and array[right]>array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heapSort(array, n):
    for i in range(n//2, -1, -1):
        heapify(array, n, i);

    for i in range(n-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


def partition(l, r, nums):
	# Last element will be the pivot and the first element the pointer
	pivot, ptr = nums[r], l
	for i in range(l, r):
		if nums[i] <= pivot:
			# Swapping values smaller than the pivot to the front
			nums[i], nums[ptr] = nums[ptr], nums[i]
			ptr += 1
	# Finally swapping the last element with the pointer indexed number
	nums[ptr], nums[r] = nums[r], nums[ptr]
	return ptr

def quickSort(l, r, nums):
	if len(nums) == 1: # Terminating Condition for recursion. VERY IMPORTANT!
		return nums
	if l < r:
		pi = partition(l, r, nums)
		quickSort(l, pi-1, nums) # Recursively sorting the left values
		quickSort(pi+1, r, nums) # Recursively sorting the right values
	return nums


def bubbleSort(arr):
	n = len(arr)
	# optimize code, so if the array is already sorted, it doesn't need
	# to go through the entire process
	swapped = False
	# Traverse through all array elements
	for i in range(n-1):
		# range(n) also work but outer loop will
		# repeat one time more than needed.
		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			# if we haven't needed to make a single swap, we
			# can just exit the main loop.
			return


def shellSort(arr):

	# Start with a big gap, then reduce the gap
	n = len(arr)
	gap = n//2

	# Do a gapped insertion sort for this gap size.
	# The first gap elements a[0..gap-1] are already in gapped
	# order keep adding one more element until the entire array
	# is gap sorted
	while gap > 0:

		for i in range(gap,n):

			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = arr[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and arr[j-gap] >temp:
				arr[j] = arr[j-gap]
				j -= gap

			# put temp (the original a[i]) in its correct location
			arr[j] = temp
		gap //= 2

