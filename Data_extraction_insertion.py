# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:39:27 2017

@author: aditya
"""
''' data extraction and insertion using python'''

import numpy as np
import pandas as pd

#accessing data from a csv file
d = pd.read_csv('/home/aditya/Data-Science-python/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv')

print d[0:5]['AREA NAME']

#write a data to .csv file

d = {'c1':pd.Series(['a', 'b', 'c']), 'c2':pd.Series([1,2., 3.,4.])}

df = pd.DataFrame(d)
df.to_csv('/home/aditya/Data-Science-python/sample_data.csv') 



