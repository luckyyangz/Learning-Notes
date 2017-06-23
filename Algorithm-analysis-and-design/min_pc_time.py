# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 01:59:07 2016

@author: jiao
"""

import numpy as np
import pandas as pd

def min_pc_time(p,f):
    n = len(p)
    data = np.zeros((n,3))
    for i in range(n):
        data[i][0] = i
        data[i][1] = p[i]
        data[i][2] = f[i]
    data = pd.DataFrame(data)
    # sort according to f[i], ascending=False
    data = data.sort([2],ascending=False)
    return data[0]
#    data = np.asarray(data)
#    return data[:0]
    
p = [2,3,4,8,4]
f = [24,6,2,5,7]
r = min_pc_time(p,f) # r is the sequence
print r