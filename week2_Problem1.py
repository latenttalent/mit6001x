#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 23:30:59 2018

@author: shreyas
"""

"""
#Problem 1
balance = 5000     
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

for month in range(12):
    monthlyPayment = (monthlyPaymentRate * balance)
    balance = (balance - monthlyPayment) + ((annualInterestRate/12) * (balance - monthlyPayment))

print("Remaining balance: " + str(round(balance,2)))

#Problem 2
annualInterestRate = 0.18
balance = 10000
monthlyPayment = balance//12//100*100
remainingBalance = balance
while remainingBalance > 0:
    remainingBalance = balance
    monthlyPayment += 10
    for month in range(12):
        remainingBalance = (remainingBalance - monthlyPayment) + ((annualInterestRate/12) * (remainingBalance - monthlyPayment))
print("Lowest Payment: " + str(monthlyPayment))
"""

#Problem 3
annualInterestRate = 0.18
balance = 999999
lowerBound = balance/12
upperBound = (balance*((1+(annualInterestRate/12))**12))/12
monthlyPayment = round((lowerBound + upperBound)/2, 2)
remainingBalance = balance
while remainingBalance > 0 or remainingBalance < -0.12:
    remainingBalance = balance
    for month in range(12):
        remainingBalance = (remainingBalance - monthlyPayment) + ((annualInterestRate/12) * (remainingBalance - monthlyPayment))    
    if remainingBalance > 0:
        lowerBound = monthlyPayment
        monthlyPayment = (lowerBound + upperBound)/2
    elif remainingBalance < -0.12:
        upperBound = monthlyPayment
        monthlyPayment = (lowerBound + upperBound)/2
print("Lowest Payment: " + str(round(monthlyPayment, 2)))