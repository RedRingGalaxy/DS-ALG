def sort(itemlist):
	swap = True
	#Loop until no Swaps
	n = 0
	while swap:
		swap = False
		#Loop through every element in a list 
		for i in range(len(itemlist)-1):
			#Check items in current and next index
			#If item in current index is grater than next index then sawp the items and make sawp as True
			if itemlist[i] > itemlist[i+1]:
				temp = itemlist[i]
				itemlist[i] = itemlist[i+1]
				itemlist[i+1] = temp
				swap = True
			n +=  1;
	return itemlist , n

if __name__ == "__main__":
	#Get user input and convert it into integer list
	user_input = list([int(i) for i in input("Enter list of number separated by space: ").split()])
	
	#Print output
	i, j = sort(user_input)
	print(f"Here we sort number in ASC order {i} . It took {j} scan time to sort.")