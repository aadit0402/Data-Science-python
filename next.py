# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 23:03:53 2018

@author: aditya
"""

import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python", "./rtftotxt.py"], stdout=output);