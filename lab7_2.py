#! python
# coding: utf-8

s = input('Давай сюди шось, і я скажу чи це паліндром\r\n')

s = s.replace(' ', '')
s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace('`', '')
s = s.replace('*', '')
s = s.replace('-', '')
s = s.replace('_', '')
s = s.lower()

print(s)

if s == s[::-1]:
	print(True)
else:
	print(False)



