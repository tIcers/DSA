from functools import reduce

nums = (16, 2, 19, 22, 10, 23, 16, 2, 27, 29, 19, 26, 12, 20, 16, 29, 6, 2, 12, 20)

filtered_numbers = filter(lambda x: x % 2 == 0, nums)
print(tuple(filtered_numbers))

mapped_numbers = map(lambda x: x * 3, nums)
print(tuple(mapped_numbers))

sum = reduce(lambda x, y: x + y, nums)
print(sum)
