# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:12:08 2025

@author: Test
"""

# import modules

import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# define variables

sample_rate = 5000 # Sampling rate in Hz
L_overhang_length = 0.1 # Overhang lengh in m
q_mass_per_unit_length = 0.2 # mass per unit length in Kg/m
I_second_moment_of_area = 2.5e-12 # second moment of area in m ** 4

#%%


df1 = pd.DataFrame(
    {
     'A': [1, 1.5, 2, 2.5, 3, 3.5], 
     'B': [4,5,6,0,0,0], 
     'C':[7,8,9,0,0,0]
     }
    ) 


arr1 = np.array((1,2,3))




df_100mm1 = pd.read_csv('100mm(1).csv', names = ['100mm_1'])




np_100mm1 = np.genfromtxt('100mm(1).csv')
np_100mm2 = np.genfromtxt('100mm(2).csv')
np_100mm3 = np.genfromtxt('100mm(3).csv')

# Compare np array lengths (1D) to identify shortest

data_points = [len(np_100mm1), len(np_100mm2), len(np_100mm3)]

smallest_data_points = min(data_points)

# index each column to [:smallest_data_points - 1]

np_100mm = np.column_stack(
    (np_100mm1, np_100mm2, np_100mm3)
    )



df_100mm = pd.DataFrame(np_100mm, columns = ['1','2','3'])



df_100mm.plot()

plt.show()

#%%
df_110mm1 = pd.read_csv('110mm(1).csv', names = ['110mm_1'])

np_110mm1 = np.genfromtxt('110mm(1).csv')
np_110mm2 = np.genfromtxt('110mm(2).csv')
np_110mm3 = np.genfromtxt('110mm(3).csv')





np_110mm = np.column_stack(
    (np_110mm1[:24990], np_110mm2[:24990], np_110mm3[:24990])
    )



df_110mm = pd.DataFrame(np_110mm, columns = ['1','2','3'])



df_110mm.plot()
plt.show

#%%

def read_and_plot(length_tens_column):
    
    length_value = '1' + str(length_tens_column) + '0mm'
    
    # Remake df_100mm1 = pd.read_csv('100mm(1).csv', names = ['100mm_1']) using the variables length_value and filename_end
    
    #df_100mm1 = pd.read_csv(length_value + '(1).csv', names = ['100mm_1'])
    
    np_array_1_with_adc =  np.genfromtxt(length_value + '(1).csv')
    
    # Remove DC component by subtracting the mean
    np_array_1 = np_array_1_with_adc - np.mean(np_array_1_with_adc)
    
    np_array_2_with_adc =  np.genfromtxt(length_value + '(2).csv')
    
    np_array_2 = np_array_2_with_adc - np.mean(np_array_2_with_adc)
    
    np_array_3_with_adc =  np.genfromtxt(length_value + '(3).csv')

    np_array_3 = np_array_3_with_adc - np.mean(np_array_3_with_adc)
    
    # Analysis will be performed for data in short segment following spike - final and initital data can be discared
    # Truncate to maximum final index
    
    # Compare np array lengths (1D) to identify shortest

    data_points = [len(np_array_1), len(np_array_2), len(np_array_3)]
    
        
    if min(data_points) == max(data_points):
        
        np_complete_array = np.column_stack((np_array_1, np_array_2, np_array_3))   
    
    else: 
        
        truncation_index = min(data_points) - 1
        np_complete_array = np.column_stack(
            (np_array_1[:truncation_index], np_array_2[:truncation_index], np_array_3[:truncation_index])
            )        

    df_complete = pd.DataFrame(np_complete_array, columns = ['1','2','3'])

    df_complete.plot()
    
    plt.title(str(length_value))
    
    plt.savefig(str(length_value), dpi = 400)
    
    plt.show()

    
    return df_complete
    

#%%

# The program failed upon reaching this line

# Isolate point of failure in a new cell
# To allow for debugging and solution testing

# Changed truncation to check for length difference and preserve data where possible

df_100mm = read_and_plot(0)
df_110mm = read_and_plot(1)
df_120mm = read_and_plot(2)
df_130mm = read_and_plot(3)
df_140mm = read_and_plot(4)

#%%




# To use curve fit we need to define our own function to fit
# p0 is the initial guesses for A, w, p, c

# Plot adc values as a function of index values from 1 (via np.arange)

def sinfunc(index, A, w, p, c):  
    return A * np.sin(w*index + p) + c


opt, pcov = curve_fit(sinfunc, np.arange(1, len(df_100mm) + 1), df_100mm['1'], p0=(1,1,1,1))

# opt = optimized A, w, p, c
# pcov = covariance matrix

index_vals_from_1 = np.arange(1, len(df_100mm) +1)
optimised_data = sinfunc(index_vals_from_1, opt[0], opt[1], opt[2], opt[3])

plt.plot(index_vals_from_1, df_100mm['1'])
plt.plot(index_vals_from_1, optimised_data)

plt.show()



