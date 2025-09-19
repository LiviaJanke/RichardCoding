# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 12:13:39 2025

@author: Test
"""

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

params = {
   'axes.labelsize': 10,
   'font.size': 10,
   'legend.fontsize': 15,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'figure.figsize': [6, 4],
   'lines.linewidth': 0,
   'axes.grid': True,
   'lines.marker': 'x'
   } 
plt.rcParams.update(params)

#%%

R1_manual = 0.5 * (6.9-0.7) / (0.43)

def resistance_formula(V1, V2, I):
    res = 0.5 * (V1 - V2) / I
    
    return res
    

R1 = resistance_formula(6.9, 0.7, 0.43)

#%%

v1 = 6.9
v1_err = 0.5

v2 = 0.7
v2_err = 0.1

I_val = 0.43
I_err = 0.03

#%%

R1_max = resistance_formula(v1+v1_err, v2-v2_err, I_val - I_err)
R1_min = resistance_formula(v1-v1_err, v2+v2_err, I_val + I_err)

diff_min = R1-R1_min
diff_max = R1_max - R1

#%%

# Calculating resistance via linear fit

I_meas, V_meas = np.loadtxt('C:/Users/Test/Richard_Coding/RichardCoding/ComputingSessionTwo/Data/Resistors.csv',
                            unpack=True, skiprows = 2, delimiter = ',')

#%%

plt.plot(I_meas, V_meas)
plt.title('PD vs I')
plt.show()


# Try adapting a linear fit to this plot from the session 10_09.py file


#%%

fit_vals, cov = np.polyfit(I_meas, V_meas ,deg = 2, cov = True)

Volt_test = np.linspace(I_meas[0], I_meas[-1], 100)

#%%

pVolts = np.poly1d(fit_vals)

ideal_volts_res = pVolts(Volt_test)

#%%

plt.plot(Volt_test, ideal_volts_res, label = 'fit')
plt.plot(I_meas, V_meas, marker = '.', label = 'real')
plt.legend()
plt.savefig('PD_I fit', dpi = 400)
plt.show()

#%%

uncert_x_sq = np.sqrt(cov[0,0]) / fit_vals[0]
uncert_x = np.sqrt(cov[1,1]) / fit_vals[1]
#uncert_const = np.sqrt(cov[2,2]) / fit_vals[2]










