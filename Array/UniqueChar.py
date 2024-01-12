# Problem
#
# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

def uni_char(s):
    seen = set()

    for string in s:
        if string in seen:
            return False
        else:
            seen.add(string)
    return True

class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
t = TestUnique()
t.test(uni_char)


