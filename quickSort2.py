def quickSort(numbers, start, end):
	
	if start >= end:
		return

	left = start
	right = end
	
	pivot = (start + end) // 2
	
	pivotValue = numbers[pivot]	

	while left <= right:
		while left <= right and numbers[left] < pivotValue :
			left += 1
		while left <= right and numbers[right] > pivotValue:
			right -= 1
		if left <= right:
			numbers[left], numbers[right] = numbers[right], numbers[left]
			left += 1
			right -= 1
	
	quickSort(numbers,start,right)
	quickSort(numbers,left,end)

arr = [20, 61, 51, 14, 42]

print(arr)
quickSort(arr,0,len(arr)-1)
print(arr)