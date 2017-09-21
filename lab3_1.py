#! python
# coding: utf-8

def add(a,b):
	return int(a) + int(b)
	
n1 = input('Дай число\r\n')

n2 = input('Давай ще одне\r\n')

n3 = add(n1,n2)

print('Тримай суму\r\n' + str(n3))