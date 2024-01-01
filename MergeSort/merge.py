def merge_sort(items):
    if len(items) <= 1: return items
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]
    left_sorted, right_sorted = merge_sort(left_split) , merge_sort(right_split)
    return merge(left_split, right_split)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left

    if right:
        result += right 
    return result
