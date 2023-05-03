#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:33:57 2021

@author: prantogg
"""


import pandas as pd

data = pd.read_csv('adult.data', names=['Age','Workclass','fnlwgt','Education','Education-num','Marital-status','Occupation','Relationship','Race','Sex','Capital-gain','Capital-loss','Hours-per-week','Native-country'])
print(data)
