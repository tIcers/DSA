# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search(search_list):
    maximum_score_index = None
    for idx in range(len(search_list)):
        if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
            maximum_score_index = idx
    return maximum_score_index
    print(search_list[idx])
    #if search_list[idx] == target_value:
    #  return idx
  #raise ValueError("{0} not in list".format(target_value))

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)


