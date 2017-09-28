#! python
# coding: utf-8

door = input('Дай мені розміри дверей (Висота Ширина) \r\n').split()

if (len(door) < 2) | (len(door) >= 3):
	print('Нєєєє братіш. Мене не обдуриш. Давай ще раз.\r\n')
	exit()

if int(door[0]) > int(door[1]):
	h = int(door[0])
	w = int(door[1])
else:
	h = int(door[1])
	w = int(door[0])
	
box = input('Дай мені розміри коробки (Всі три)\r\n').split();
	
if len(box) < 3:
	print('Нєєєє братіш. Мене не обдуриш. Давай ще раз.\r\n')
	exit()
	
a = int(box[0])
b = int(box[1])
c = int(box[2])

if (a <= h) & (b <= w):
	print('IT FITS. YAY.')
elif(b <= h) & (a <= w):
	print('IT FITS. YAY.')
elif(c <= h) & (b <= w):
	print('IT FITS. YAY.')
elif(a <= h) & (c <= w):
	print('IT FITS. YAY.')
elif(b <= h) & (c <= w):
	print('IT FITS. YAY.')
elif(c <= h) & (a <= w):
	print('IT FITS. YAY.')
else:
	print('Your box is too fat!')