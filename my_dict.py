d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(type(d), d)

for k, v in d.items():
    print(k, '-->', v)

for el in d:
    print(el)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for el in d.items():
    print(el)
    print(el[0], '-', el[1])
