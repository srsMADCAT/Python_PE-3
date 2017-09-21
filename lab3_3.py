#! python
# coding: utf-8

def BMI(m,h):
	return float(m) / (float(h) ** 2)
	
hight = float(input('Який в тебе зріст? \r\n'))

#тут можна було зробити перевірку на те яке число введене
#наприклад якщо число більше ~5 - ділити його на 100, щоб з
#сантиметрів получити метри. Але я інженер і я лінивий

#BUT....

if hight > 5:
	hight = hight/100

#Ну вот... зробив...

mass = input('Круто! А вага?\r\n')

bmi = BMI(mass,hight)

print('Дивись який ти жирний\r\n' + str(bmi))