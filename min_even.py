import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10, 10))
print(numbers)

is_init = False
for x in numbers:
    if x % 2 == 0:
        if not is_init:
            min_even = x
            is_init = True
        elif min_even > x:
            min_even = x
if is_init:
    counter = 0
    for x in numbers:
        if x == min_even:
            counter += 1
    print('Min even is', min_even, 'Counter:', counter)
else:
    print('No such elements...')
