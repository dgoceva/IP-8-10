# 10 digits + 26 small latin letters + 26 capital latin letters
import string
base = string.digits + string.ascii_letters

# print(base)
a = int(input('Input number:'))
b = int(input('Input base:'))
# print(a, b)

result = ''
while a != 0:
    result += base[a % b]
    a //= b
print(result[::-1])
