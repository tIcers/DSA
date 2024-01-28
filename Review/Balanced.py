def balance_check(s):
    close_to_open = {'}':'{', ']':'[', ')':'('}
    stack = []

    for string in s:
        if stack and string in close_to_open:
            stack.pop()
        else:
            stack.append(string)
    return len(stack) == 0

