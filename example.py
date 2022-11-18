number = int(input('Count:'))

numbers = []
for _ in range(number):
    n = int(input('Number:'))
    numbers.append(n)

print(max(numbers))

numbers = [int(n) for n in input('List:').split()]
print(max(numbers))

numbers = map(int, input('List:').split())
print(max(numbers))
