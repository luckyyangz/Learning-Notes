# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 21:04:45 2016

@author: Jiao
"""

class Problem:
    def __init__(self):
        self.z=0
        self.A=[]
        self.b=[]
        self.c=[]
    def pivot(Bi,self,e,l):
        self.b[l]/=self.A[e][l]
        for j in range(len(self.A)):
            self.A[j][l]/=self.A[e][l]
        for i in range(len(self.b)):
            if i!=l:
                self.b[i] -=self.b[l]*self.A[e][i]
                for j in range(len(self.A)):
                    self.A[j][i]=self.A[j][i]-self.A[j][l]*self.A[e][i]
        self.z=self.z-self.b[l]*self.c[e]
        for j in range(len(self.A)):
            self.c[j]-=self.c[e]*self.A[j][l]
         
def initializeSimplex(Bi,problem):
    mindex=10000#,-1
    minIndex=-1
    for i in range(len(problem.b)):
        if problem.b[i]<mindex:
            mindex=problem.b[i]
            minIndex=i
    for i in range(len(problem.b)):
        Bi.append(i+len(problem.b))
#    if 
def simplex(Bi,problem):
    (Bi,problem)=initializeSimplex(problem)
           
        
            
            


  
  
