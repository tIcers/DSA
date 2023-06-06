
def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    print(search_list[idx])
    if search_list[idx] == target_value:
      return idx
  raise ValueError(f"{target_value} not in list")



values = [54, 22, 46, 99]
print(linear_search(values, 22))
