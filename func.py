def create_list(el, ll=[]):
    ll.append(el)
    return ll


def create_list1(el, ll=None):
    if ll is None:
        ll = []
    ll.append(el)
    return ll


def sum_it(*args):
    return sum(args)


def concat_it(*args):
    return ','.join(args)


print(create_list(1))
print(create_list(2))
print(create_list(3))

print(create_list1(1))
print(create_list1(2))
print(create_list1(3))

print(sum_it(1, 2, 3))
print(sum_it(1, 2))
print(sum_it(1))

print(concat_it('ime', 'suma', 'dlyvnost'))
print(concat_it('Ivan', '1200', 'schetovoditel'))
