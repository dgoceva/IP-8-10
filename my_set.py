s = set([1, 2, 3, 4])
print(type(s), s)
# s[0] = 44
s.add(44)
s.add(11)
print(s)
s.remove(2)
print(s)
s.update({3, 4, 55, -11})
print(s)
s |= {1, 2, 7}  # s = s | {1,2,7}  union e |
print(s)
s &= {1, 2, 3, 4, 5}
print(s)

us = frozenset([1, 2, 3, 4, 5])
print(type(us), us)
# us.add(44)
# us.add(11)
# print(us)
# us.remove(2)
# print(us)
# us.update({3, 4, 55, -11})
# print(us)
us |= {1, 2, 7}
print(us)
us &= {1, 2, 3, 4, 5}
print(us)
