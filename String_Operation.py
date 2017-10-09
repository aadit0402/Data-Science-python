# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:21:29 2017

@author: aditya
"""


import numpy as np
import pandas as pd

#accessing data from a csv file
d = pd.read_csv('/home/aditya/Data-Science-python/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv')

print d['AREA NAME'][0:5]

#extract first word from the area name column
print d['AREA NAME'][0:5].str.extract('(\w+)')
