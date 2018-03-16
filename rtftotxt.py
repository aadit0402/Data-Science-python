# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 22:45:12 2018

@author: aditya
"""

from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

doc = Rtf15Reader.read(open('/home/aditya/Downloads/aaaa.rtf'))

print PlaintextWriter.write(doc).getvalue()