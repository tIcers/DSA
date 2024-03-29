from ast import Index
import sys

n = 50

data = []

for i in range(n):
    a = len(data)

    b = sys.getsizeof(data)

    print('Length: {0:3d} Size in bytes: {1:4d}'.format(a, b))

    data.append(n)

import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0  # actual elements
        self.capacity = 1  # cap for array
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        """return element at index k"""
        if not 0 <= k < self.n:
            return IndexError("k is out of bounds")

        return self.A[k]

    def append(self, ele):
        """add element to end of the array"""
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # double capacity if not enough room

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):  # reference all existing values
            B[k] = self.A[k]

        self.A = B  # call A the new bigger array
        self.capacity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()


"""
Given two stings, check to see if they are anagrams

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"
"""


def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


from nose.tools import assert_equal


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


"""
Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)
would return 2 pairs:

 (1,3)
 (2,2)"""


def pair_sum(arr, k):
    seen = set()
    ouput = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            ouput.add((min(num, target), max(num, target)))

    return len(ouput)


"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([3,7,2,1,4,6])[1,2,3,4,5,6,7],
Output:

5 is the missing number"""


def finder(arr1, arr2):
    arr1 = arr1.sort()
    arr2 = arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]
