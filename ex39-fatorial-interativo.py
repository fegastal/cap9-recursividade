def fact_in(n):
    stack = Stack()
    factorial = 1
    while n > 0:
        stack.push(n)
        n = n - 1
    while not stack.isempty():
        factorial = factorial * stack.pop()
    return factorial