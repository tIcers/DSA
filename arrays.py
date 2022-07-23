from ast import Index
import sys

n = 50

data= []

for i in range(n):
    a = len(data)
    
    b = sys.getsizeof(data)
    
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    
    data.append(n)


import ctypes

class DynamicArray(object):

	def __init__(self):
		self.n = 0 # actual elements
		self.capacity = 1 # cap for array
		self.A = self.make_array(self.capacity)

	def __len__(self):
		return self.n 

	def __getitem__(self,k):
		"""return element at index k"""
		if not 0 <= k < self.n:
			return IndexError("k is out of bounds")

		return self.A[k]

	def append(self,ele):
		"""add element to end of the array"""
		if self.n == self.capacity:
			self._resize(2 * self.capacity) # double capacity if not enough room

		self.A[self.n] = ele 
		self.n +=1

	def _resize(self,new_cap):
		B = self.make_array(new_cap)

		for k in range(self.n): # reference all existing values
			B[k] = self.A[k]

		self.A = B # call A the new bigger array
		self.capacity = new_cap

	def make_array(self,new_cap):
        
		return (new_cap * ctypes.py_object)()

