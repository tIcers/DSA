import csv
from functools import reduce


def count(predicate, iterable):
    count_filter = filter(predicate, iterable)
    count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
    return count_reduce


def average(itr):
    iterable = iter(itr)
    return average_helper(0, iterable, 0)


def average_helper(curr_count, itr, curr_sum):
    next_sum = next(itr, "null")
    if next_sum == "null":
        return curr_sum / curr_count
    curr_count += 1
    curr_sum += next_sum
    return average_helper(curr_count, itr, curr_sum)


with open("1kSalesRec.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    fields = next(reader)
    count_belgium = count(lambda x: x[1] == "Belgium", reader)
    print(count_belgium)
    csvfile.seek(0)
    avg_portugal = average(
        map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader))
    )
    print(avg_portugal)
