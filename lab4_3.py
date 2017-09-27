#! python
# coding: utf-8

import decimal

pay = decimal.Decimal(input('Вкажіть свою зарплатню\r\n'))

tax1 = pay * decimal.Decimal('0.18')

tax2 = pay * decimal.Decimal('0.015')

print('Ви ще нічо не зробили, а вже винні державі ' + str(tax1+tax2) + ' гривень')