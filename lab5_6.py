#! python
# coding: utf-8

data=input('Давай сюди сторони трикутника \r\n').split()

a = int(data[0])
b = int(data[1])
c = int(data[2])

if (a + b >= c) and (a + c >= b) and (c + b >= a):
	print('Таки може існувати')
else:
	print('Таки такого бути не може')