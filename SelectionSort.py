def selectSort(list):
	for i in range(len(list)):
		curr_ind = i
		for j in range(i,len(list)):
			if list[curr_ind] > list[j]:
				curr_ind = j
		if curr_ind != i:
			temp = list[i]
			list[i] = list[curr_ind]
			list[curr_ind] = temp
			
		print(list[i])
	return list		
 
if __name__ == "__main__":
	print(selectSort([int(i) for i in input().split()]))