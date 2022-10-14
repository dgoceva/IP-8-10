from random import randint

numbers = []
for i in range(20):
    numbers.append(randint(-100, 100))
print(numbers)
print(min(numbers), '+', max(numbers), '=', min(numbers)+max(numbers))
