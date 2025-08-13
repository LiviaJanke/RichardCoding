# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 14:01:54 2025

@author: Test
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

#%%

params = {
   'axes.labelsize': 10,
   'font.size': 10,
   'legend.fontsize': 15,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'figure.figsize': [6, 4],
   #'lines.linewidth': 0,
   'lines.marker': 'x'
   } 
plt.rcParams.update(params)

#%%

data = np.loadtxt(
    'C:/Users/Test/Richard_Coding/RichardCoding/ComputingSessionTwo/Data/Dataset.txt'
    )# read the data from file
plt.ylabel("Number of measurements")# set the y-label
plt.xlabel("Speed (10e8 m/s)")# set the x-label
plt.hist(data)# create a histogram of the data
plt.grid()
plt.savefig('Speed of Light Measurements', dpi = 400)
plt.show()# show the plot


#%%

# Library is a set of keys and values, queried via library_name['key']
library_of_cats = {'Robert':'cat', 'Anthony':'dog'}

#i.e. to find the value for the key 'Robert':
library_of_cats['Robert']

#%%

# Find the mean and standard deviation of the speed values

avg = np.mean(data)
sample_std = np.std(data, ddof = 1)
sample_std_err = sample_std / np.sqrt(len(data))

#%%

plt.ylabel("Number of measurements")# set the y-label
plt.xlabel("Speed (10e8 m/s)")# set the x-label
plt.hist(data)# create a histogram of the data
plt.grid()
plt.savefig('Speed of Light Measurements', dpi = 400)
plt.show()# show the plot

#%%

Temp, Res_Cu, Res_Al = np.genfromtxt('C:/Users/Test/Richard_Coding/RichardCoding/ComputingSessionOne/Resistivity.txt', unpack = True)

#%%

Cu_err = np.std(Res_Cu) / np.sqrt(len(Res_Cu))

Al_err = np.std(Res_Al) / np.sqrt(len(Res_Al))

plt.errorbar(Temp, Res_Cu, yerr = Cu_err,linewidth =0, marker = 'x', 
             elinewidth = 1, capsize = 2, capthick = 1)
plt.linewidth = 0
plt.show()


#%%


Set1, Set2, Set3, Set4, Set5 = np.genfromtxt(
    'C:/Users/Test/Richard_Coding/RichardCoding/ComputingSessionTwo/Data/five_datasets.txt', unpack = True, skip_header = 1)

def find_errors(dataset):
    
    std_err = np.std(dataset) / np.sqrt(len(dataset))
    
    return dataset, std_err

vals_1, err_1 = find_errors(Set1)
vals_2, err_2 = find_errors(Set2)
vals_3, err_3 = find_errors(Set2)
vals_4, err_4 = find_errors(Set2)
vals_5, err_5 = find_errors(Set2)

fig, axs = plt.subplots(5, sharex = 'col')
plt.xlabel('Speed')
axs[0] = plt.subplot(5,1,1)
axs[0].hist(Set1)
axs[1] = plt.subplot(5,1,2)
axs[1].hist(Set2)
axs[2] = plt.subplot(5,1,3)
axs[2].hist(Set3)
axs[3] = plt.subplot(5,1,4)
axs[3].hist(Set4)
axs[4] = plt.subplot(5,1,5)
axs[4].hist(Set5)
plt.show()


#%%

# Checking for outliers - 2.5 standard deviations beyond the mean
# standard error is the uncertainty of a sample mean
# standard deviation is the error on individual datapoints


def remove_outliers(dataset):
    
    std_err = np.std(dataset, ddof =1) / np.sqrt(len(dataset))
    print(std_err)
    mean = np.mean(dataset)
    lower_limit = mean - (2.5 * np.std(dataset))
    print(lower_limit)
    upper_limit = mean + (2.5 * np.std(dataset))
    print(upper_limit)
    
    clean_dataset = []
        
    for i in dataset:
        if i > upper_limit:
            print(i)
        elif i < lower_limit:
            print(i)
        else:
            clean_dataset.append(i)
            
    return clean_dataset

clean_set1 = remove_outliers(Set1)
clean_set2 = remove_outliers(Set2)
clean_set3 = remove_outliers(Set3)
clean_set4 = remove_outliers(Set4)
clean_set5 = remove_outliers(Set5)

#%%

clean_data = remove_outliers(data)

plt.ylabel("Number of measurements")# set the y-label
plt.xlabel("Speed (10e8 m/s)")# set the x-label
plt.hist(clean_data)# create a histogram of the data
plt.grid()
plt.savefig('Speed of Light Measurements', dpi = 400)
plt.show()# show the plot

#%%

# Figure out how to put errorbars on histograms 
# For next session

