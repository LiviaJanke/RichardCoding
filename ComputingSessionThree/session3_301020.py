# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:20:36 2020

@author: Admin
"""

#%%

# An example function, that takes two inputs variables x, y, adds them together and then
# squares their sum. 
# Different ways the function can be called and how arguements are passed to it are shown.

# Define the function here:
#def square_two_numbers(x,y):
 #   z=(x+y)**2 # This is the arithmetic calculation
  #  return z # The value of z is returned to the main program

# Below this is the main program.

# One way of calling the function is with two integers.
# Note: the result of the function (i.e. the value of z) is stored in the variable result_ints.
#result_ints=square_two_numbers('fish','sea') 
#print(result_ints)

# Now we call the function with two floats. 
#result_floats=square_two_numbers(4.2,2.3)
#print(result_floats)

# This time we create two variables, one a float and the other an integer.
#num1=5.3
#num2=10
# We call the function using the variables we created, instead of using literals. 
#result_mixed=square_two_numbers(num1,num2)
#print(result_mixed)

w = 5

def square_two_numbers_add_w(x,y):
    w = 2
    z = (x+y)**2 + w
    return z

squared = square_two_numbers_add_w(5,7)    
print(squared)

#%%

def force_between_masses(m1,m2,x1,x2):
    G = 6.67 * (10**(-11))
    F = (G*m1*m2)/((x1-x2)**2) 
    return F


initial = force_between_masses(1, 1, 1, 1.00000001)
print(initial)

#%%

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def quadratic_roots(a,b,c):    
    root1 = (-b + np.sqrt(((b**2)-(4*a*c))))/(2*a)
    root2 = (-b -np.sqrt(((b**2)-(4*a*c))))/(2*a)
    return root1, root2


first_try = quadratic_roots(4, 5, 13)
print(first_try)






























