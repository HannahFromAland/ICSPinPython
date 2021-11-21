#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:54:22 2021

@author: Yuan
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
portion_down_payment = 0.25

r = 0.04

month_salary = annual_salary / 12
current_savings = 0
num_of_month = 0

while (current_savings < total_cost * portion_down_payment):
     current_savings = current_savings*(1+r/12)
     current_savings += month_salary * portion_saved
     num_of_month += 1
     if num_of_month % 6 == 0:
         month_salary += semi_annual_raise * month_salary
     
print("Number of months: ", num_of_month)