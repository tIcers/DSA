class Recursion:
    def __init__(self) -> None:
        pass
    def sum_to_one(n):
        result = 1
        call_stack = []

        while n != 1:
            execution_context = {"n_value": n}
            call_stack.append(execution_context)
            n -= 1
            print(call_stack)
        print("base case reached")

        return result, call_stack
