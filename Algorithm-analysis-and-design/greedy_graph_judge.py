# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 01:39:27 2016

@author: jiao
"""

def greedy_graph_jugde(s):
    n = len(s)
    s = sorted(s, reverse=True)
    if s[0]==0:
        return True
    elif s[-1]<0:
        return False
    else:
        k = s[0]
        n = n-1
        if(k > n):
            return False
        s = s[1:]
        for i in range(k):
            s[i] = s[i]-1
    return greedy_graph_jugde(s)
        
s = [3,3,2,2] #example
r = greedy_graph_jugde(s)
print r
        