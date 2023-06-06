
def binary_search(sorted_list, target):
    if sorted_list == []:
        return 'value not found'
    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx] 
    if mid_val == target:
        return mid_idx
    if mid_val > target:
        left_half = sorted_list[:mid_idx] 
        return binary_search(left_half, target)
    if mid_val < target:
        right_half = sorted_list[mid_idx + 1:]
        result = binary_search(right_half, target)
        if result == 'value not found':
            return result
        else:
            return result + mid_idx + 1


# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 17))


# realized above code is wasteful because it's making copy of N/2 elements where N i sthe length of the sorted list at each recursive call
# so i willl implement code using pointer
def binary_search(sorted_list, left_pointer, right_pointer, target):
    if left_pointer >= right_pointer: # reached an empty sublist
        return 'value not found'

    mid_idx = (left_pointer + right_pointer) //2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    if mid_val > target:
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))

