from cProfile import label
import imp
import timeit
from math import log

from django.forms import inlineformset_factory
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inlineformset_factory

plt.style.use('bmh')

n =  np.linespace(1,10,100)
labels = ['constant','log','liner','log linear','quadratic','cubic','exp']
big_o = [np.ones(n.shape),np.log(n),n,n*np.log(n),n**2,n**2,2**n]

plt.figure(figsize=(12,10))
plt.ylim(0,50)

#plt setup 
for i in range(len(big_o)):
	plt.plot(n,big_o[i],label= labels[i])

plt.legend(loc=0)
plt.ylabel('relevant runtime')
plt.xlabel('n')

"""
Get number and return sum of numbers
if n == 10, return 55
"""


def sum1(n):
	sums = 0
	for x in range(n+1):
		sums += x
	return sums

print(sum1(10))

def sum2(n):
	return (n*(n+1)/2)

print(sum2(10))

%timeit sum1(100)
%timeit sum2(100)

""" 
Prints first item in a list of values.
"""
lst = [0,1,2,3,4,5,6]
def constant_function(values):
	return (values[0])

constant_function(lst)

"""Takes in list and prints out all values"""

def lst_func(lst):
	for val in lst:
		print(val)
lst_func([1,2,3])


"""Prints pairs for every item in list."""

def quad(lst):
	for item_1 in lst:
		for item_2 in lst:
			print(item_1,item_2)

lst = [0,1,2,3,4]

print(quad(lst))


"""prints all items once"""

def print_once(lst):
	for val in lst:
		print(val)

"""prints all items twice"""
#o(2n)
def print_twice(lst):
	for val in lst:
		print(val)

	for val in lst:
		print(val)

"""
Make function that prints first item O(1)
	prints the first 1/2 of the list 
	then prints a string 10 times
"""

def midpoint(lst):
	print(lst[0]) # first sentence # o(1)

	mid_point = len(lst) / 2

	for val in lst[:mid_point]:
		print(val) # this is for second sentence # o(n/2)

	for i in range(10):
		print("WOW!") # this is for third one # o(n)

	# o (1 + (n/2) + n) = o(n)? if n is getting closer to inf

	



