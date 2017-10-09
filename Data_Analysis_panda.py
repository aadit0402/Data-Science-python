# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 19:54:11 2017

@author: aditya
"""

''' the data structure of pandas
    1.Series
    2.DataFrame
    3.Panel'''

import pandas as pd
import numpy as np

'''Series is a 1d array which can hold any type of data such as integer, float, string or python objects too'''
'''How to create a Series using Pandas library'''
print pd.Series(np.random.randn(5))

# we can customize the index
print pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'])

