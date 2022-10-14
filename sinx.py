from math import pi, sin

EPS = 1e-6

x = float(input('x[deg]='))
xrad = x/180*pi

sinx = 0
an_1, an = 0, xrad
counter = 3

while abs(an-an_1) >= EPS:
    sinx += an
    an_1, an = an, an*(-1)*xrad**2/((counter-1)*counter)
    counter += 2
print(f'sin({x})={sinx}\nSIN({x})={sin(xrad)}')
