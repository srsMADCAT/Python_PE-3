#! python
# coding: utf-8

def ask():
	k = input('Довжина обертання\r\n')
	return int(k)

string = input('Рядок сюди\r\n')

k = ask()

if k > (len(string)/2):
	print('Довжина обертання має бути не більше половини рядка')
	ask()
	
string = string[k:] + string[:k]

print(string)



