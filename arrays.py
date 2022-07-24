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


"""
Given two stings, check to see if they are anagrams

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"
"""

def anagram(s1,s2):
	s1 = s1.replace(" ","").lower()
	s2 = s2.replace(" ","").lower()

	return sorted(s1) == sorted(s2)


from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")