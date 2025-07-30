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

df1 = pd.DataFrame(
    {
     'A': [1, 1.5, 2, 2.5, 3, 3.5], 
     'B': [4,5,6,0,0,0], 
     'C':[7,8,9,0,0,0]
     }
    ) 

#%%

arr1 = np.array((1,2,3))


#%%

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

plt.show()

#%%










