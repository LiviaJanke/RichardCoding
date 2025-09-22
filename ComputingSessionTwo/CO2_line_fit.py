# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:08:59 2025

@author: Test
"""

import numpy as np
import pandas as pd
import scipy as sp
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt

#%%

params = {
   'axes.labelsize': 10,
   'font.size': 10,
   'legend.fontsize': 15,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'figure.figsize': [6, 4],
   'lines.linewidth': 0,
   'axes.grid': True,
   'lines.marker': '.'
   } 
plt.rcParams.update(params)


#%%

year, CO2_molfrac = np.loadtxt('C:\\Users\\Test\\Richard_Coding\\RichardCoding\\ComputingSessionTwo\\Data\\CO2_data.csv', unpack = True, skiprows = 2, delimiter=',')


#%%

plt.plot(year, CO2_molfrac)
plt.savefig('CO2_vs_year', dpi = 400)
plt.show()

#%%

fit_vals, cov_CO2 = np.polyfit(year, CO2_molfrac, deg = 2, cov = True)

years_array = np.linspace(year[0], year[-1], 2500)

pCO2 = np.poly1d(fit_vals)

CO2_array = pCO2(years_array)

plt.plot(year, CO2_molfrac, label = 'data')
plt.plot(years_array, CO2_array, label = 'polyfit', color = 'red')
plt.title('CO2 vs year')
plt.legend()
plt.xlabel('Year')
plt.ylabel('CO2 molfrac')
plt.grid()
plt.show()


#%%


#def my_sin(t,period, amplitude, phase):
#    return np.sin(t * 2 * np.pi / period + phase

def my_exp(t, exponent, factor, offset):
    return offset + factor * np.exp(t*exponent)

guess_period = 0.1
guess_amplitude = 1
guess_phase = 310
initial_guesses = [guess_period, guess_amplitude, guess_phase]

fit_exp = curve_fit(my_exp, year - year[0], CO2_molfrac, p0 = initial_guesses)

#fit = curve_fit(my_sin, year, CO2_molfrac, p0=initial_guesses)


# data_fit = my_sin(years_array, fit[0][0], fit[0][1], fit[0][2])
# does the same thing as below line
data_fit = my_exp(years_array - year[0], *fit_exp[0])

#%%

plt.plot(year, CO2_molfrac, label = 'data')
#plt.plot(years_array, CO2_array, label = 'polyfit', color = 'red')
plt.plot(years_array, data_fit, label = 'curve_fit', color = 'green')
plt.legend()
plt.title('CO2 vs year')
plt.xlabel('Year')
plt.ylabel('CO2 molfrac')
plt.grid()
plt.show()






