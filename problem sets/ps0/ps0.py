# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:09:21 2020

@author: egultekin
"""
import math

print('Enter number x: ')
x = input()
print('Enter number y: ')
y = input()
first_calc = int(x) ** int(y)
second_calc = round(math.log(int(x), 2))
print('x**y = ', first_calc)
print('log(x) = ', second_calc)
