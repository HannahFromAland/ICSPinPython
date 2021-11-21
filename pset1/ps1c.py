#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 11:19:25 2021

@author: Yuan
"""
def month_need(month_salary,portion_saved):
    current_savings = 0
    
    for m in range(36):
        if m > 0 and m % 6 == 0:
            month_salary += 0.07 * month_salary
        current_savings = current_savings*(1+0.04/12)
        current_savings += month_salary * portion_saved     
    return current_savings

annual_salary = float(input("Enter your annual salary: "))

month_salary = annual_salary / 12
low = 0
high = 10000
num_guesses = 0
flag = True
guess = (high + low) / 2.0

while abs(month_need(month_salary, guess/10000)-250000) > 100:
    if month_need(month_salary, guess/10000) - 250000 > 100:
        high = guess
    else:
        low = guess
    guess = (high + low)/2.0
    if low == high:
        print("It is not possible to pay the down payment in three years.")
        flag = False
        break
    num_guesses += 1
if flag:
    print("Best saving rate:", guess/10000)
    print("Steps in bisection search:", num_guesses)
    