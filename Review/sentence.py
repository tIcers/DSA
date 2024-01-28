def rev_word(s):
    splited_s = s.split()
    splited_s.reverse()
    return splited_s
# this is not good approach because it's python stuff...

def rev_word(s):
    space = ' '
    word = []
    length = len(s)

    i = 0

    while i < length:
        if s[i] != space:
            word_start = i

            while i < length and s[i] != space:
                i += 1
            word.append(s[word_start:i])
        i += 1
    return " ".join(reversed(word))
