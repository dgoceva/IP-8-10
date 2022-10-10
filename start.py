import random
sum = 0

for i in range(5):
    # x = int(input("x="))
    x = random.randint(-100, 100)
    print(x, end=' ')
    sum += x
print()
print(sum)
