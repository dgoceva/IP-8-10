t1 = 123
t2 = 123,
print(t1, t2)
print(type(t1), type(t2))
t1 = (123)
print(t1, type(t1))
t1 = (123,)
print(t1, type(t1))
print(len(t1))
# print(t1[0], t1[1])
print(t1[0])
# t1[0] = 'hi'

t1 = [1, 2, 3], [4, 5, 6]
print(t1, type(t1))
t1[0].append(21)
t1[0].append(111)
print(t1, type(t1))

t1[0][0] = [11, 22]
print(t1)

t1[1].insert(0, 33)
print(t1)

x, y = t1
print(x, type(x))
