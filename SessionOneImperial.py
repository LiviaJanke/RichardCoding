# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 14:13:19 2025

@author: Test
"""

import numpy as np
import pandas as pd

#%%

# Different ways of reading data into numpy
# numoy loadtxt - most basic,

resistivity_data_txt = np.loadtxt('Resistivity.txt', usecols = 1, skiprows = 5)
# newest version assumes whitespace

#%%



resistivity_data_txt_v2 = np.genfromtxt('Resistivity.txt', usecols = 1, skip_header = 5)
