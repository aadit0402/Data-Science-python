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

# Series from a python dict 

d = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
print pd.Series(d)

'''Added comment here to test. It is just for learning purpose'''
'''DataFrame is a 2d structure with columns that can be of different datatypes. (table)'''
'''A dataFrame can be formed from following data structure a numpy array, list, dicts, series, a 2d numpy array'''
#using dict

d = {'c1':pd.Series(['a', 'b', 'c']), 'c2':pd.Series([1,2., 3.,4.])} #here bydefault index 0,1,2 ... is generated but we can manually set the index
df = pd.DataFrame(d)
print df

'''panel is a data structure that handles 3d data'''
d = {'Item1': pd.DataFrame(np.random.randn(4,3)), 
     'Item2': pd.DataFrame(np.random.randn(4,2))}
print pd.Panel(d)



