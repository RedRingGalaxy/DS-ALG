def radixSort(array):
	max_ele = max(array)
	
	place = 1
	
	while max_ele // place > 0:
		countingSort(array,place)
		place *= 10
		
def countingSort(array,place):
	size = len(array)
	
	count = [0] * 10
	
	output = [0] * size
	
	for i in range(0, size):
		index =  array[i] // place
		count[index % 10] += 1
		
	for i in range(1,10):
		count[i] += count[i -1]
		
	i = len(array) -1
	while i >= 0:
		index = array[i] // place
		output[count[index % 10] -1] = array[i]
		count[index % 10] -= 1
		i -= 1
		
		
	for i in range(size):
		array[i] = output[i]

if __name__ == "__main__":
	array = [121, 432, 564, 23, 1, 45, 788]
	radixSort(array)
	print(array)