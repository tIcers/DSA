# find pair sum for target k, and show the unique pair
def pair_sum(arr, k):
    seen = set()
    output = set()
    
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))
    print('\n'.join(map(str, list(output))))

# find missing number  from arr2 which is shuffled and compare with arr1
def finder(arr1, arr2):
    counter = {}

    for num in arr1:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

    for num in arr2:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] -= 1

    for key, value in counter.items():
        if value != 0:
            return key

# this is another solution using default dict
import collections

def finder2(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2: d[num] +=1 

    for num in arr1: 
        if d[num] == 0: return num 
        else: d[num] -= 1

# another solution for finder (which i did not come up....)
def finder3(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        result ^= num ## this is XOR
    return result


# Problem => Giver an array of intergers (postive and negative) find the largest countinous sum

def large_count_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum = current_sum = 0
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

# Sentence Reversal
# Problem
#
# Given a string of words, reverse all the words. For example:
#
# Given:
#
# 'This is the best'
#
# Return:
#
# 'best the is This'
#
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
#
# '  space here'  and 'space here      '
#
# both become:
#
# 'here space'


def rev_word(s):
    words = []
    i = 0

    while i < len(s):
        if s[i] != ' ':
            word_start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            words.append(s[word_start:i])
        i += 1

    return " ".join(reversed(words))

# ## Problem
#
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 
#
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.


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


# Unique Characters in String
# Problem
#
# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

def uni_char(s):
    if s == '': 
        return True
    seen = set()

    for letter in s:
        if letter in seen:
            return False
        else:
            seen.add(letter)
    return True
