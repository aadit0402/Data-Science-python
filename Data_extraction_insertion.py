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

'''to read and write data from xls file, xlrd and xlwt package should be installed for pandas'''
#d = pd.read_excel('path of the xls file')
#df.to_excel('location of file where you want to write the data)
''' to read data from a JSON file, json package can be used 
    import json
    json_data = open('filename')
    data = json.load(filename)
    json_data.close()'''
    
#we can manually assign the row name and column name
df = pd.DataFrame(np.random.randn(5,3), index=['a0','a10','a20','a30','a40'], columns=['x', 'y', 'z'])
print df

df = df.reindex(['a0','a1', 'a10', 'a11', 'a20', 'a21', 'a30', 'a31', 'a40', 'a41'])
print df

#filling NULL value

#df.fillna(2) #donot know this is not working
print df.fillna(2) #its working



