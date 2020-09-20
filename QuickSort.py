def QuickSort(Itemlist,l,h):
	if l < h:
		pivot = Partition(Itemlist,l,h)
		QuickSort(Itemlist,l,pivot-1)
		QuickSort(Itemlist,pivot+1,h)

def Partition(Itemlist,l,h):
	pivot = Itemlist[h]
	p1 = l - 1
	
	for i in range(l,h):
		if Itemlist[i] <= pivot:
			p1 += 1
			(Itemlist[p1] , Itemlist[i]) = (Itemlist[i], Itemlist[p1])
			
	(Itemlist[p1+1],Itemlist[h]) = (Itemlist[h], Itemlist[p1+1])
	
	return p1+1
	

if __name__ == "__main__":
	arr = [1,1,7,3,8,5,5]
	QuickSort(arr,0,6)
	print(arr)