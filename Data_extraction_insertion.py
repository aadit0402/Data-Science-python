# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:39:27 2017

@author: aditya
"""
''' data extraction and insertion using python'''

import numpy as np
import pandas as pd

d = pd.read_csv('/home/aditya/Data-Science-python/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv')

print d[0:5]['AREA NAME']

