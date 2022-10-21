def fib(n=5):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(b)
        a, b = b, a+b
    return result


print(fib(10))
print(fib(20))
print(fib())
