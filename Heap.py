class Heap:
	def __init__(self):
		self.arr = []
	
	def insert(self, val):
		size = len(self.arr)
		if size == 0:
			self.arr.append(val)
		else:
			self.arr.append(val)
			
			for i in range(size//2-1,-1,-1):
				self.heapify(self.arr, size, i)
			
	def delete(self):
		self.arr[0], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[0]
		
		val = self.arr.pop()
		
		for i in range((len(self.arr)//2)-1,-1,-1):
			self.heapify(self.arr, len(self.arr)-1, i)
			
		return val
			
	def heapify(self, arr, n, i):
		large = i
		left = 2 * i + 1
		right = 2 * i + 2
		
		if left <= n and arr[i] < arr[left]:
			large = left
			
		if right <= n and arr[large] < arr[right]:
			large = right
			
		if large != i:
			arr[i], arr[large] = arr[large], arr[i]
			self.heapify(arr, n, large)
			
if __name__ == "__main__":
	h = Heap()
	h.insert(1)
	h.insert(2)
	h.insert(5)
	h.insert(4)
	h.insert(2)
	h.insert(6)
	h.insert(9)
	print(h.arr)
	
	arr = []
	for i in range(len(h.arr)):
		arr.append(h.delete())
		
	print(arr)
