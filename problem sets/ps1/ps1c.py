# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:18:24 2020

@author: egultekin
"""






def calcTotalSaving(annualSalary, savingRate, roi, semiAnnualRaise):
    monthPassed = 0
    # this first guess is your saving rate, calculate your total savings in 36 months with this guess (saving rate)
    totalSaving = 0
    monthlySaving = (annualSalary / 12) * savingRate
    # first month where there is no return from investment
    totalSaving = totalSaving + monthlySaving
    monthPassed += 1
    
    # remaining 35 months (monthly saving, return from investment, salary raise every 6 months)
    for month in range(2, 37):
        # incrementing total saving by roi
        totalSaving = totalSaving * (1 + (roi / 12))
        # increasing total saving by monthly saving
        totalSaving += monthlySaving
        monthPassed += 1
        # updating annual salary and monthly saving semi annually
        if month % 6 == 0:
            annualSalary = annualSalary * (1 + semiAnnualRaise)
            monthlySaving = (annualSalary / 12) * savingRate

    return totalSaving



def findSavingRate(annualSalary, downPaymentNeeded, roi, semiAnnualRaise):
    # initialize local variables
    
    # epsilon
    epsilon = 10
    
    # num of guesses
    numGuesses = 0
    
    # binary search variables: low, high, initial guess = mid point in search space
    # savings rate range: 0 - 1
    low = 0
    high = 1
    guess = (high + low) / 2.0
    
    #calculate total savings usıng initial guess
    totalSaving = calcTotalSaving(annualSalary, guess, roi, semiAnnualRaise)
    
    # execute binary search: update your guess by comparing the total savings to the expected result, guess will always be the middle point of our search space
    # If total savıngs below result, then we need to increase our guess, which means we ll need to search ın the upper half of the search space
    # and vice versa
    while abs(totalSaving - downPaymentNeeded) >= epsilon:
        if totalSaving < downPaymentNeeded:
            # look in the upper half search space
            low = guess
        else:
            # look in the lower half search space
            high = guess
        # next guess is halfway in the new search space
        guess = (high + low) / 2.0
        numGuesses += 1
    
        ###calculating total saving with the new guess
        totalSaving = calcTotalSaving(annualSalary, guess, roi, semiAnnualRaise)
    
    # once we reach a satisfactory result, exit the loop and return the result
    return guess, numGuesses


def main():
    # annual salary
    annualSalary = float(input('Enter your annual salary: '))
    
    # salary raise every six months
    semiAnnualRaise = float(input('Enter your semi annual raise: '))
    
    # annual return of investments
    roi = float(input('Enter your annual return on investment: '))
    
    # portion of down payment needed for the house
    downPayment = float(input('Enter your portion of down payment for the house: '))
    
    # total cost of the house
    totalCost = float(input('Enter total cost of the house: '))
    
    # down payment needed for the house
    downPaymentNeeded = totalCost * downPayment
    
    # calculate saving rate
    savingRate, numGuesses = findSavingRate(annualSalary, downPaymentNeeded, roi, semiAnnualRaise)
    
    # print the output
    print('number of guesses =', numGuesses)
    print('Your saving rate should be ' + str(savingRate))
    
    
    
    
    
main()
    










