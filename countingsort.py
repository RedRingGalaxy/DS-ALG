def countingSort(array):
	max = 9
	size = len(array)
	
	output = [0] * size
	
	count = [0] * (max +2)
	
	for i in range(0,size):
		count[array[i]] +=1
		
	for i in range(len(count)):
		count[i] += count[i-1]
	
	i = size - 1
	while i >= 0:
		output[count[array[i]]-1] = array[i]
		count[array[i]] -= 1
		i -= 1
	
	for i in range(size):
		array[i] = output[i]

if __name__ == "__main__":
	array = [1, 4, 1, 5, 9, 8, 5, 3]
	countingSort(array)
	print(array)