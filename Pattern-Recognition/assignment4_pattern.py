# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:28:55 2016

@author: Jiao
"""

import numpy as np 
import pandas as pd


fx=0
fx_df=1
def outlin(x,df): #输出层激励函数sigmod
    fx=1/(1+np.exp(-x))
    if df==0:      
        return fx
    elif df==1:                                                                                                                 
        fx_df=fx*(1+fx)
        return fx_df 
def inlin(x,df):  #隐含层激励函数tanh函数 
    fx=np.tanh(x)
    if df==0:      
        return fx
    elif df==1:
        fx_df=1-fx**2
        return fx_df 

c1=np.array([[ 1.58, 2.32, -5.8], [ 0.67, 1.58, -4.78], [ 1.04, 1.01, -3.63],
[-1.49, 2.18, -3.39], [-0.41, 1.21, -4.73], [1.39, 3.16, 2.87],
[ 1.20, 1.40, -1.89], [-0.92, 1.44, -3.22], [ 0.45, 1.33, -4.38],
[-0.76, 0.84, -1.96]])
c2=np.array([[ 0.21, 0.03, -2.21], [ 0.37, 0.28, -1.8], [ 0.18, 1.22, 0.16],
[-0.24, 0.93, -1.01], [-1.18, 0.39, -0.39], [0.74, 0.96, -1.16],
[-0.38, 1.94, -0.48], [0.02, 0.72, -0.17], [ 0.44, 1.31, -0.14],
[ 0.46, 1.49, 0.68]])
c3=np.array([[-1.54, 1.17, 0.64], [5.41, 3.45, -1.33], [ 1.55, 0.99, 2.69],
[1.86, 3.19, 1.51], [1.68, 1.79, -0.87], [3.51, -0.22, -1.39],
[1.40, -0.44, -0.92], [0.44, 0.83, 1.97], [ 0.25, 0.68, -0.99],
[ 0.66, -0.45, 0.08]])
x=np.concatenate((c1,c2,c3))
x_set=np.ones([30,1])
x=np.column_stack((x_set,x))
y_set=np.ones([10,1])
y=np.concatenate((y_set,2*y_set,3*y_set))
n_H=5
learn_rate=0.1
criter_angel=0.001
np.random.seed(1) 
w_ih=2*np.random.random((4,n_H))-1 #3*4 #4*5
w_hj=2*np.random.random((n_H,3))-1 #4*1   #5*3
for i in range(2000):
    random=np.random.randint(0,30)
    L0_x=x[random]    
    L1_net=np.dot(w_ih.T,L0_x) #5*1
    L1_y=inlin(L1_net,fx)      #5*1
    L2_net=np.dot(w_hj.T,L1_y) #3*1
    L2_z=outlin(L2_net,fx)     #3*1
    error_j=outlin(L2_net,fx_df)*(y[random]-L2_z)  #3*1
    error_j.shape=(3,1)
    L1_y.shape=(5,1)
    L1_net.shape=(5,1)
    w_hj+=learn_rate*np.dot(L1_y,error_j.T)    #5*3    
    error_h=inlin(L1_net,fx_df)*(np.dot(w_hj,error_j))  #5*1
    error_h.shape=(5,1)
    L0_x.shape=(4,1)
    w_ih+=learn_rate*np.dot(L0_x,error_h.T)        #4*5
    error=0.5*np.sum((y[random]-L2_z)**2)
    print error
    if error<criter_angel:
        print "训练次数:",i,"  收敛误差:",error
        break