import math

EPS = 1e-6

pi = 0
sign = -1
counter = 3
an_1, an = 0, 1

while abs(an-an_1) >= EPS:
    pi += an
    an_1, an = an, sign/counter
    sign *= -1
    counter += 2
pi *= 4
print('pi={0}\nPI={1}'.format(pi, math.pi))
