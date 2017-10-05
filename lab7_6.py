#! python
# coding: utf-8

string = input('РАМОЧКУ\r\n')

count = int(len(string))

star = '*'

print(star*(count+4) + '\r\n' + 
	star + ' ' + string + ' ' + star + '\r\n' + 
	star*(count+4))