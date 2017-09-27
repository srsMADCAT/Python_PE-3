#! python
# coding: utf-8
	
import math	

data = list(map(float, input('Дай три дійсні числа\r\n').split()))

a = data[0]
b = data[1]
c = data[2]

if (c == 0.0):
	print('На нуль ділиті нізя таваріщ')
	
f = (1/(c*math.sqrt(2*math.pi)))*math.exp(((-1)*(a-b)**2)/(2*c**2))

print(str(f))