# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:19:47 2020

@author: egultekin
"""


annual_salary = input('Enter the annual salary: ')
portion_saved = input('Enter the portion of the salary to be saved in %: ')
total_cost = input('Enter the total cost of your home: ')

# portion of total cost that is needed as down payment
portion_down_payment = 0.25

# current savings start at zero
current_savings = 0

# annual interest rate
r = 0.04

# month starts at zero 
month_passed = 0

# calculation of down payment
down_payment = float(total_cost) * portion_down_payment

# monthly saving from salary
monthly_saving = (float(annual_salary) / 12) * (float(portion_saved) / 100)

# there is no monthly return from investment the first month, only the saving
current_savings = current_savings + monthly_saving
month_passed += 1

# months required for saving up down payment
while current_savings < down_payment:
    current_savings = current_savings * (1 + (r / 12))
    current_savings += monthly_saving
    month_passed += 1
else:
    year_passed = month_passed // 12
    month_passed = month_passed % 12
    print('You can save up for a down payment in ' + str(year_passed) + ' year(s) and ' + str(month_passed) + ' month(s)')