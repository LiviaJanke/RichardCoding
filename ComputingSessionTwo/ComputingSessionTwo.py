# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 13:32:04 2025

@author: Test
"""

import numpy as np

A = np.array([10,20,30,40,50,60,70,80,90,100])

#%%

# What values do the following slices select?


q1 = A[-1]
# -1 selects the final value in the array

q2 = A[1:3]
# selects values from and including start index to but not including end index
# i.e. indices 1, 2 in this example
# Notation = [Start:Stop:Step]

q3 = A[1:]
#Selects all values from index 1 to end inclusive

q4 = A[:5]
# Selects all values up to but not including index 5

q5 = A[0:6:2]
# Every second value between 0 - 6 (not including 6)

q6 = A[::2]
# Every second value from whole array


#%%

# Can create 2D or higher dimensional arrays by nesting 1D arrays

twoDarray=np.array([[1,2],[10,20],[100,200]])
print(twoDarray)

# To slice a 2D array we need to specify [row index, column index]



#%%

arange = np.arange(0,50,1)

# numpy arange function - returns values from (start, stop, step)

linspace = np.linspace(0, 50,50)

# Evenly spaced number of values from start up to and including stop values

#%%

array_multiplication = arange * linspace

#%%

x=np.array([0.76,0.79,0.84,0.75,0.80,0.79])
mean_value=np.mean(x)
print('The mean value is:', mean_value, 'm')


#%%

# To find the sample standard deviation:
std = np.std(x, ddof = 1)
print(std)

# to find the standard error of the mean:
    
std_err_mean = np.std(x, ddof=1) / np.sqrt(len(x))

#dividing sample standard deviation by square root of sample size.


#%%

# Use unpack = True to load in columns separately
c1, c2, c3 = np.loadtxt(
    'C:/Users/Test/Richard_Coding/RichardCoding/ComputingSessionOne/Resistivity.txt',
    unpack = True)

np.savetxt('C:/Users/Test/Richard_Coding/RichardCoding/ComputingSessionOne/c1.txt',c1)


#%%

combined_1 = [c1, c2, c3]
combined_2 = np.column_stack([c1, c2, c3])
print(combined_1, combined_2)






