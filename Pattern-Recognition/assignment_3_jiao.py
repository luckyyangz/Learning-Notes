# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:23:04 2016

@author: Jiao
"""
import numpy as np
import matplotlib.pyplot as plt
def data_all():
    w1=np.array([[1,1,1,1,1,1,1,1,1,1],[0.1,6.8,-3.5,2.0,4.1,3.1,-0.8,0.9,5.0,3.9],[1.1,7.1,-4.1,2.7,2.8,5.0,-1.3,1.2,6.4,4.0]])
    w2=np.array([[1,1,1,1,1,1,1,1,1,1],[7.1,-1.4,4.5,6.3,4.2,1.4,2.4,2.5,8.4,4.1],[4.2,-4.3,0.0,1.6,1.9,-3.2,-4.0,-6.1,3.7,-2.2]])
    w3=np.array([[1,1,1,1,1,1,1,1,1,1],[-3.0,0.5,2.9,-0.1,-4.0,-1.3,-3.4,-4.1,-5.1,1.9],[-2.9,8.7,2.1,5.2,2.2,3.7,6.2,3.4,1.6,5.1]])
    w4=np.array([[1,1,1,1,1,1,1,1,1,1],[-2.0,-8.9,-4.2,-8.5,-6.7,-0.5,-5.3,-8.7,-7.1,-8.0],[-8.4,0.2,-7.7,-3.2,-4.0,-9.2,-6.7,-6.4,-9.7,-6.3]])
    h1=w1.T;h2=w2.T;h3=w3.T;h4=w4.T
    return h1,h2,h3,h4
def data_load(w1,w2):
    w1=list(w1);w2=list(w2*(-1))
    w1.extend(w2)
    y=np.array(w1)
    return y
def  convergence_count(y):
    a=np.zeros([1,3])
    k=0
    m=0;w=0#计算迭代次数
    while 1:
        for i in range(len(y)):
            if np.dot(a,(y[i].T))<=0:
                w=w+y[i]
            else:
                k=k+1
        a=w+a
        print a
        if k>=y.shape[0]:
            print "iteration finish=",m
            return m
            break
        else:
            k=0
            m+=1
            w=0
'''--------第1题a--------'''
#'''-------输入数据w1,w2---'''
#y=data_load(w1,w2)
#w1w2_count=convergence_count(y)  #w1,w2需要迭代23次
'''---------第1题b---------'''
#'''--------输入数据是w2,w3---'''
#y=data_load(w2,w3)
#w2w3_count=convergence_count(y)  # w2,w3需要迭代16次
'''---------------------第2题w1,w3-----------'''
#y=data_load(w1,w3)
#a1,b1=Ho_Kashyap(k_max,b_min,y)
'''---------------------第2题w2,w4-----------'''
#y=data_load(w2,w4)
#a2,b2=Ho_Kashyap(k_max,b_min,y)

def k_min_count(e,b_min):
    e=np.abs(e)
    k=0
    for i in range(len(e)):
        if e[i]<b_min:
            k+=1
    if k==len(e):
        return 1
    else:
        return 0

def Ho_Kashyap(k_max,b_min,y):
    a=np.ones([3,1])
    b=np.zeros([20,1])
    I=np.eye(3)
    r=0.01
    Y1=np.linalg.inv(np.dot(y.T,y)+r*I)
    YY=np.dot(Y1,y.T)
    count_times=0
    while 1:
        for k in range(k_max):
            e=np.dot(y,a)-b
            ee=0.5*(e+np.abs(e))
            b=b+2*ee
            a=np.dot(YY,b)
            count_times+=1
            if k_min_count(e,b_min):
                print "iteration times=",count_times
                return a,b
                break
        if count_times>=k_max:
            print "No solution found!"
            break
        else :
            break
def  relaxation_margin(b,y):
    a=np.zeros([1,3])
    k=0
    m=0;w=0#计算迭代次数
    error=0
    count_k=[]
    count_error=[]
    while 1:
        for i in range(len(y)):
            if np.dot(a,(y[i].T))-b<=0:
                w+=y[i]*(np.dot(a,y[i].T)-b)/((y[i]**2).sum())
                error+=0.5*((np.dot(a,y[i].T)-b)**2)/((y[i]**2).sum())
            else:
                k=k+1
        count_error.append(error)
        count_k.append(m)
        a=a-w
        print "error=",error
        if k>=y.shape[0]:
            print "iteration finish=",m
            return a,m,count_k,count_error
            break
        else:
            k=0
            m+=1
            w=0
            error=0
            
'''  
本次作业采用if elif方式构成switch的作用
若第1题a，则令switch_ch=1
若第1题b，则令switch_ch=2
若第2题w1和w3，则令switch_ch=3
若第2题w2和w4，则令switch_ch=4
若第3题a，则令switch_ch=5
若第3题b，则令switch_ch=6
''' 

switch_ch=4                      ####修改此处，即可得本次作业的各题目结果          
k_max=1000
b_min=1
w1,w2,w3,w4=data_all()
if switch_ch==1:                     #第1题w1,w2
    y=data_load(w1,w2)
    w1w2_count=convergence_count(y)  
    pass   
elif switch_ch==2:                   #第2题w2,w3 
    y=data_load(w2,w3)
    w2w3_count=convergence_count(y)  
    pass   
elif switch_ch==3:                   #第2题w1,w3 
    y=data_load(w1,w3)
    Ho_Kashyap(k_max,b_min,y)
    pass
elif switch_ch==4:                   #第2题w2,w4- 
    y=data_load(w2,w4)
    a2,b2=Ho_Kashyap(k_max,b_min,y)
    pass
elif switch_ch==5:                   #第3题w1,w3,b=0.1 
    y=data_load(w1,w3)
    b=0.1
    a,m,count_k,count_error=relaxation_margin(b,y)
    line,=plt.plot(count_k[:40],count_error[:40])
    pass
elif switch_ch==6:                   #第3题w1,w3,b=0.5 
    y=data_load(w1,w3)
    b=0.5
    a,m,count_k,count_error=relaxation_margin(b,y)
    line,=plt.plot(count_k,count_error)
    pass