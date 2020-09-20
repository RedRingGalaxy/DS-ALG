def bucketSort(array):
	bucket= []
	
	for i in range(len(array)):
		bucket.append([])
		
	for i in range(len(array)):
		index = int(10 * array[i])
		bucket[index].append(array[i])
		
	for i in bucket:
		i.sort()
	
	k =0	
	for i in range(0,len(array)):
		for j in bucket[i]:
			array[k] = j
			k +=1
			
	return array

if __name__ == "__main__":
	data = [.42, .32, .33, .52, .37, .47, .51]
	print(bucketSort(data))