def fib(n):
    a, b = 0, 1
    result = []
    while a <= n:
        result.append(a)
        a, b = b, a+b
    return result


def fib2(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == '__main__':
    import sys
    print(sys.argv)
    print(fib(int(sys.argv[1])))
    print(sys.path)
