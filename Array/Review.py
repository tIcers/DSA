# find pair sum for target k, and show the unique pair
def pair_sum(arr, k):
    seen = set()
    output = set()
    
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))
    print('\n'.join(map(str, list(output))))

# find missing number  from arr2 which is shuffled and compare with arr1
def finder(arr1, arr2):
    counter = {}

    for num in arr1:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

    for num in arr2:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] -= 1

    for key, value in counter.items():
        if value != 0:
            return key

# this is another solution using default dict
import collections

def finder2(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2: d[num] +=1 

    for num in arr1: 
        if d[num] == 0: return num 
        else: d[num] -= 1

# another solution for finder (which i did not come up....)
def finder3(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        result ^= num ## this is XOR
    return result


# Problem => Giver an array of intergers (postive and negative) find the largest countinous sum

def large_count_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum = current_sum = 0
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

