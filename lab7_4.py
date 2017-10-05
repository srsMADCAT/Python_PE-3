#! python
# coding: utf-8

string = input('Давай щось шифрувати\r\n')

decrypted=''

for i in string:
	decrypted=decrypted+chr(ord(i)+1)

print(decrypted)

