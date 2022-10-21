numbers = input().split()
print(numbers)

even = [int(el) for el in numbers if sum(map(int, el)) % 2 == 0]
print(even)

print(sum(even))

# ----------------------
n = int(input('n='))
numbers = []
for _ in range(n):
    x = int(input())
    numbers.append(x)

sum = 0
for el in numbers:
    sum_digit = 0
    x = el
    while x > 0:
        sum_digit += x % 10
        x //= 10
    if sum_digit % 2 == 0:
        sum += el

print(sum)
