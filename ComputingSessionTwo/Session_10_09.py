# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 13:03:54 2025

@author: Test
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import scipy as sp

from scipy.optimize import curve_fit

#%%

noisy_df = pd.read_csv('Data/noisy_data.txt', delimiter = ' ',
                       names = ['Temp', 'Cu', 'Al'])
Al = noisy_df['Al']
#pd.read_csv can be used for all sorts of files

#%%

Temp, Cu, Cu_err = np.loadtxt('Data/noisy_data.txt', delimiter = ' ',unpack = True)

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
   'lines.marker': 'x'
   } 
plt.rcParams.update(params)

#%%


plt.plot(Temp, Cu, label = 'Cu')
plt.plot(Temp, Al, label = 'Al')
plt.legend()
plt.show()

#%%


def find_error(data):
    avg = np.mean(data)
    sample_std = np.std(data, ddof = 1)
    # ddof is 1 because this is a discrete set of data points
    sample_std_err = sample_std / np.sqrt(len(data))
    return sample_std_err

err_Cu = find_error(Cu)
err_Al = find_error(Al)

#%%

plt.errorbar(Temp, Cu, yerr = err_Cu, label = 'Cu', capsize = 1,
             elinewidth = 1)
plt.errorbar(Temp, Al, yerr = err_Al, label = 'Al', capsize = 1,
             elinewidth = 1)
plt.legend()
plt.savefig('Resistivity', dpi = 400)
plt.show()


#%%

fit_vals, cov_Cu = np.polyfit(Temp, Cu,deg = 2, w = 1/Cu_err, cov = True)

# setting degree too high risks overfitting

uncert_x3 = np.sqrt(cov_Cu[0,0])
# square root of covariance matrix diagonals give uncertainty of each fitting parameter 
# ie standard deviation

Temp_test = np.linspace(Temp[0], Temp[-1], 100)

pCu = np.poly1d(fit_vals)

ideal_res_Cu = pCu(Temp_test)

plt.errorbar(Temp, Cu, yerr = err_Cu, label = 'Cu', capsize = 1,
             elinewidth = 1)
plt.plot(Temp_test, ideal_res_Cu, marker = '.')
plt.legend()
plt.savefig('Resistivity fit', dpi = 400)
plt.show()

#%%







