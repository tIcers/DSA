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