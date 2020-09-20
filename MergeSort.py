def MergeSort(Itemlist,s,e):
	if s < e:
		mid = (s+e)//2
		MergeSort(Itemlist,s,mid)
		MergeSort(Itemlist,mid+1,e)
		Merge(Itemlist,s,mid,e)
	
def Merge(Itemlist,s,mid,e):
	print(s,mid,e)
	n1 = mid - s + 1
	n2 = e - mid
	
	sub1 = []
	sub2 = []
	
	for i in range(n1):
		sub1.append(Itemlist[s+i])

	for i in range(n1):
		sub2.append(Itemlist[mid+1+i])
	
		
	i = 0
	j = 0
	k = s
	while( (i < n1) and (j < n2)):
		print(sub1,sub2,i,j)
		if sub1[i] < sub2[j]:
			Itemlist[k] = sub1[i]
			i += 1
		else:
			Itemlist[k] = sub2[j]
			j += 1
		k += 1
		
		
	while i < n1:
		Itemlist[k] = sub1[i]
		i += 1
		k += 1
		
	while j < n2:
		Itemlist[k] = sub2[j]
		j += 1
		k += 1
		

if __name__ == "__main__":
	ls = [3,1,4,2]
	MergeSort(ls,0,3)
	print(ls)