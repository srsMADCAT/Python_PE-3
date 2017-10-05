#! python
# coding: utf-8

string = input('Давай рахувати англійські голосні\r\n')

string = string.lower()
temp = ['a', 'o', 'u', 'i', 'e', 'y']
count = 0
for i in string:
	if i in temp:
		count+=1
print(count)