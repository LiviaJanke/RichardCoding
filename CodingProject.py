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

#%%

"""

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


np_100mm = np.column_stack(
    (np_100mm1[:24990], np_100mm2[:24990], np_100mm3[:24990])
    )



df_100mm = pd.DataFrame(np_100mm, columns = ['1','2','3'])



df_100mm.plot()

plt.show()



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
"""
#%%

"""

We are recreating:
    
    
    num_samples = len(df1) # Number of samples in the data
    duration = num_samples / sample_rate # Total duration of the signal
    time = np.linspace(0, duration, num_samples) # Time axis
    # Extract ADC values from the data
    adc_values = df1['ADC_Value'].values

    # Remove DC component by subtracting the mean
    dc_component = np.mean(adc_values)
    signal_remove_dc = adc_values - dc_component

"""

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
    
    # Need to fix indexing solution - truncation used currently 

    np_complete_array = np.column_stack(
        (np_array_1[:24990], np_array_2[:24990], np_array_3[:24990])
        )



    df_complete = pd.DataFrame(np_complete_array, columns = ['1','2','3'])

    df_complete.plot()
    
    plt.title(str(length_value))

    plt.show()

    
    return df_complete
    

#%%

df_100mm = read_and_plot(0)
df_110mm = read_and_plot(1)
df_120mm = read_and_plot(2)
df_130mm = read_and_plot(3)
df_140mm = read_and_plot(4)

#%%




