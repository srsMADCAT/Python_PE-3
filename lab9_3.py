#python3
# coding=utf-8

lang = list()

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
	'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
	'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
	'8':'---..', '9':'----.', '0':'-----'}
	
string = input('Давай сюди позначення\r\n')
string = string.upper()

for i in range(len(string)):
	lang.append(morse.get(string[i]))
	
print(''.join(lang))
	
