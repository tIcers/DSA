# ## Problem
#
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 
#
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.




class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        assert_equal(sol(''), '')

        # Test Case 2: String with Repeated Characters
        assert_equal(sol('AABBCC'), 'A2B2C2')

        # Test Case 3: String with Mixed Repeated Characters
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')

        # Test Case 4: String with Unique Characters
        assert_equal(sol('abc'), 'a1b1c1')

        # Test Case 5: String with All Same Characters
        assert_equal(sol('aaaa'), 'a4')

        print('ALL TEST CASES PASSED')


def compress(s):
    count = {}

    for letter in s:
        if letter not in count:
            count[letter] = 1
        elif letter in count:
            count[letter] +=1 

    compressed = ''
    for key, value in count.items():
        compressed += f'{key}{value}'
    return compressed

# Run Tests
t = TestCompress()
t.test(compress)
