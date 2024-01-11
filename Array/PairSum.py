# Problem
#
# Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.
#
# So the input:
#
# pair_sum([1,3,2,2],4)
#
# would return 2 pairs:
#
#  (1,3)
#  (2,2)
#

def pair_sum(arr, k):
    if len(arr) < 2:
        return 
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(target)
        else:
            output.add( (min(num, target), max(num, target)))
    return len(output)
