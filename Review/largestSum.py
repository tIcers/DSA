def largest_count_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum, current_sum = arr[0], arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum



