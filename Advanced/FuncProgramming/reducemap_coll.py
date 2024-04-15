from functools import reduce

fruits = {
    "Grape": (4, 6, 2),
    "Lemon": (7, 3, 1),
    "Orange": (5, 8, 1),
    "Apple": (2, 8, 10),
    "Watermelon": (0, 9, 6),
}

total_fruits = reduce(
    lambda x, y: x + y,
    map(lambda x: fruits[x][0] + fruits[x][1] + fruits[x][2], fruits),
)
