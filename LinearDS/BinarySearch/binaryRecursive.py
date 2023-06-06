
def binary_search(sorted_list, target):
    if sorted_list == []:
        return 'value not found'
    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx] 
    if mid_val == target:
        return mid_idx
    return mid_idx, mid_val


# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
