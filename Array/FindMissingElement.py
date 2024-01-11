# # Find the Missing Element
#
# ## Problem
#
# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array. 
#
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
#
# Input:
#     
#     finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
#
# Output:
#
#     5 is the missing number
#
#

def finder(arr1, arr2):
    sorted_arr1 = sorted([num for num in arr1])
    sorted_arr2 = sorted([num for num in arr2])
    i = 0
    for num in sorted_arr2:
        if num == sorted_arr1[i]:
            i += 1
            continue
        elif num != sorted_arr1[i]:
            print(sorted_arr1[i])
            return sorted_arr1[i]
    return


arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
finder(arr1,arr2)


class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

t = TestFinder()
t.test(finder)
