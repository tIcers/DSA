import csv
from collections import namedtuple
from functools import reduce

tree = namedtuple("tree", ["index", "width", "height", "volume"])

with open("tree.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    next(reader)

    mapper = map(
        lambda x: tree(int(x[0]), float(x[1]), int(x[2].strip()), (float(x[3]))),
        reader,
    )

    t = filter(lambda x: x.height > 75, mapper)
    trees = tuple(t)
    widest = reduce(lambda x, y: x if x.width > y.width else y, trees)

    print(trees)
    print(widest)
