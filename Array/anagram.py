from nose.tools import assert_equal
#
# ## Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 
#
# For example:
#
#     "public relations" is an anagram of "crap built on lies."
#     
#     "clint eastwood" is an anagram of "old west action"
#     
# **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**


def anagram(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return True


    sorted_s1 = sorted([char for char in s1 if char != ' '])
    sorted_s2 = sorted([char for char in s2 if char != ' '])
    return sorted_s1 == sorted_s2


class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

t = AnagramTest()
t.test(anagram)


def anagram2(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in s2:
        if char in count:
            count[char] -= 1
        else: 
            count[char] = 1

    for k in count:
        if count[k] != 0: return False

    return True

    

