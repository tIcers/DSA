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

# [Hi John,are you ready to go?]
# rev_word('   ')
# rev_word('         space before')
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
