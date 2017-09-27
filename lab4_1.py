#! python
# coding: utf-8
	
import math	
	
data = list(map(float, input('Дай два невід*ємні дійсні числа\r\n').split()))

a = data[0]
b = data[1]

if (a < 0.0) | (b <= 0.0):
	print('Нене дядя, не вийде. Я таке передбачив. Від*ємні нізя. І друге число нуль тоже нізя')
	exit()
	
x = (math.sqrt(a*b))/(math.exp(a)*b) + a*(math.exp((2*a)/b))

print(str(x))
