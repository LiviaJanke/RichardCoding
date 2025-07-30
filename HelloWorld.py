# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 14:47:56 2025

@author: Test
"""

#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy as sp

#%%


# this is a comment

print('Hello World')

# this is a string 

print('Again')

#%%

string_to_print = 'Hello World'

float_to_print = 5.9

int_to_print = 9

bool_to_print = True

char_to_print = '!'


#%%

div = int(20 / 3)

mod = 20 % 3

numbers = [5.9, 3.2, 11, 4, 2, 7, 8.9]


#%%

# Using only the numbers list
# find 2 different ways to make the number 15


numbers[5] + int(numbers[6])

#%%

# Conditional Statements

# Three types: if, elif, else

password = 'I Hate Birds'

if len(password) <= 6:
    # Counting number of characters 
    # Which includes spaces
    
    print('Too Short!')

if password == 'I Hate Birds': #my password is 'password'

    print('Birds are Great!')


#%%

# Casting

# I write my variable names in snake_case
# And my function names in CamelCase
# Do not EVER put a space in your variable name!!
# More of an issue for 'paths'

int(float_to_print)

str(float_to_print)


#%%

# I want to select the final letter from password


password[-1]

password[len(password)-1]


#%%

specialCharacters = set('$#@!*')

# Writing a function to check if a password is secure enoguh

def PasswordCheck(potential_password):
    
    if len(potential_password) <= 6:
        # Counting number of characters 
        # Which includes spaces
        
        return 'Too Short!'

    elif potential_password == 'password': #my password is 'password'

        return 'Password cannot be password'
    
    # We would need to use a dictionary/database to check for special characters
    
    # Password cannot be username
    
    elif not any(c in specialCharacters for c in password):
    
        return 'Must Use Special Characters'    
    
    else:
        
        return 'Go Ahead' + ' ' + potential_password



#%%

PasswordCheck('Richard')

# Will introduce sets, databases etc in future

 # Will look at loops later today

#%%


# Programming a calculator (integers 1 to 10)

# Planning with Pseudocode

# Aka Flowcharts


def AdditionFunc(a,b):

    # Check if a, b are unit integers
    
    return a + b

# Write a similar subtraction function

def SubtractionFunc(a,b):
    
    # Check if a, b are unit integers
    
    return a - b

def MultiplicationFunc(a,b):
    
    return a * b

def DivisionFunc(a,b):
    
    return a / b


#%%

print(AdditionFunc(10.2, 2))

SubtractionFunc(10.2, 2)


class Calculator:
    
    def __init__(self, a,b):
        self.a = a
        self.b = b
        self.sum = a + b
        self.sub = a - b
        self.multiply = a * b
        self.div = a/b

set1 = Calculator(1, 2, 3)

#%%

#Largest item

max(1,2,3)


# Smallest item

min(1,2,3)

#%%


numbers1 = [1,2,3,4,5]

numbers2 = [1.1, 2.2, 3.3, 4.4, 5.5]

#%%

max(numbers1)

max

#%%

class Student:
    
    uni_name = 'Bristol'
    
    def __init__(self, name, subject, year):
        
        self.name = name
        self.subject = subject
        self.year = year


    def good_subject_filter(self):
        
        if self.subject != 'Physics':
            
            return 'No'
        
        else:
            
            return 'Yes'
        
        

student1 = Student('Richard','EEE', '2')

#%%


class FamilyStructure:
    
    
    def __init__(self, no_of_people, lives_in, youngest_age):
        
        self.no_of_people = no_of_people
        
        self.lives_in = lives_in
        
        self.youngest_age = youngest_age




RichardFamily = FamilyStructure(3, 'Beijing', 20)

LiviaFamily = FamilyStructure(14, 'Lancaster', 3)

#%%

LiviaFamily.no_of_people - RichardFamily.no_of_people


#%%

# I have made a change!







