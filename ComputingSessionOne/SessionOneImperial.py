# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 14:13:19 2025

@author: Test
"""

import numpy as np
import pandas as pd

#%%

# Datetime 
# Use standard ISOformat of YYYY-MM-DD where possible 

from datetime import date
from datetime import timedelta 

#%%

# Different ways of reading data into numpy
# numpy loadtxt - most basic,

resistivity_data_txt = np.loadtxt('C:/Users/Test/Richard_coding/RichardCoding/Resistivity.txt')
# newest version assumes whitespace

# Can specify whole path name with forward slashes 
# Or can use os.path to add directories to search - but try to avoid this!

#%%

# numpy genfromtxt - slightly more sophisticated

resistivity_data_txt_v2 = np.genfromtxt('Resistivity.txt')


#%%


# pandas read_csv - good for large data sets

resistivity_df = pd.read_csv('Resistivity.csv', names = ['Temperature (K)', 
                                                         'Resistivity Cu Ohm m', 
                                                         'Resistivity Al Ohm m'], 
                             skiprows = 2)


# To select a column from a pandas dataframe, use the column name

df_temperatures = resistivity_df['Temperature (K)']

#%%

# Read in Car_Data. csv using the three methods discussed:

car_data_loadtxt = np.loadtxt('C:/Users/Test/Richard_coding/RichardCoding/Car_Data.csv', 
                              skiprows = 1, delimiter = ',', dtype = str)

#%%

car_data_genfromtxt = np.genfromtxt('Car_Data.csv', skip_header = 1, delimiter = ',', dtype = str)

#%% 

car_data_df = pd.read_csv('Car_Data.csv')

#%%

np.savetxt('saved data.txt', df_temperatures)


# I have changed something




