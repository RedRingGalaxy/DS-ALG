def InsertSort(itemlist):
	for i in range(1,len(itemlist)):
		Key = itemlist[i]
		j = i - 1 
		
		while( j >= 0 and Key < itemlist[j]):
			itemlist[j+1] = itemlist[j]
			j -= 1
			
		itemlist[j+1] = Key
		
	return itemlist
	
if __name__ == "__main__":
	print(InsertSort([4, 3, 2, 1, 4,3 , 2, 1]))