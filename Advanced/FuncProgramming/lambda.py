""" 
def squared(x):
  return x * x

def cubed(x):
  return x*x*x
"""


def odd_or_even(n, even_function, odd_function):
    if n % 2 == 0:
        return even_function(n)
    else:
        return odd_function(n)


square = lambda x: x * x

cube = lambda x: x * x * x

test = odd_or_even(5, cube, square)
