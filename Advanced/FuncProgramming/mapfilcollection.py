nums = (2, 12, 5, 8, 9, 3, 16, 7, 13, 19, 21, 1, 15, 4, 22, 20, 11)

greater_than_10_doubled = map(lambda x: x * 2, filter(lambda x: x > 10, nums))

functional_way = map(lambda x: x * 3, filter(lambda x: x % 3 == 0, nums))

print(tuple(greater_than_10_doubled))
print(tuple(functional_way))
