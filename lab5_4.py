#! python
# coding: utf-8

import cmath

def ans1():
	temp = ((-1)*b - cmath.sqrt(d))/(2*a)
	return temp;
def ans2():
	temp = ((-1)*b + cmath.sqrt(d))/(2*a)
	return temp;

data = input('Дай мені А, B і C і я тобі щось порахую. Можливо. \r\n').split()

a = complex(data[0])
b = complex(data[1])
c = complex(data[2])

d = b**2 - 4 * a * c


print(str(ans1()) + str(ans2()))