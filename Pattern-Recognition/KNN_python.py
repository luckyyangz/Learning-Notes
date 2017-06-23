# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:45:09 2016

@author: Jiao
"""

from mnist_python import  Mnist_import
from sklearn import neighbors
from numpy import *
import matplotlib.pyplot as plt
import datetime
import operator
import os
#from os import listdir

def main():
    trainfile_x='../../MNIST/train-images.idx3-ubyte'
    trainfile_y='../../MNIST/train-labels.idx1-ubyte'
    testfile_x='../../MNIST/t10k-images.idx3-ubyte'
    testfile_y='../../MNIST/t10k-labels.idx1-ubyte'
    train_x=Mnist_import(filename=trainfile_x).getImage()
    train_y=Mnist_import(filename=trainfile_y).getLabel()
    test_x=Mnist_import(filename=testfile_x).getImage()
    test_y=Mnist_import(filename=testfile_y).getLabel()
    
#    path_trainset="../../MNIST/image_train"
#    path_testset="../../MNIST/image_test"
#    if not os.path.exists(path_trainset):
#        os.mkdir(path_trainset)
#    if not os.path.exists(path_testset):
#        os.mkdir(path_testset)
#    Mnist_import(outpath=path_trainset).outImage(train_x,train_y)
#    Mnist_import(outpath=path_testset).outImage(test_x,test_y)
    return train_x,train_y,test_x,test_y
def testKNN():
    startTime=datetime.datetime.now()
    knn=neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(train_x,train_y)
    match=0;
    for i in xrange(len(test_y)):
        predictLabel=knn.predict(test_x[i])[0]
        if(predictLabel==test_y[i]):
            match+=1
    endTime=datetime.datetime.now()
    print 'use time: '+str(endTime-startTime)
    print 'error rate:'+str(1-(match*1.0/len(test_y)))
def classifyKNN(intx,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=tile(intx,(dataSetSize,1))-dataSet
    sqMat=diffMat**2
    sqDistances=sqMat.sum(axis=1)
    distances=sqDistances**0.5
    sortDataIndex=distances.argsort() #数组值从小到大的索引
    classCount={}
    for i in range(k):
        voteLabels=labels[sortDataIndex[i]]
        classCount[int(voteLabels)]=classCount.get(int(voteLabels),0)+1
        #classCount.iteritems()迭代输出字典的键对值；在sorted中使用按照字典的第二个域进行排序，reverse=Ture表示倒序,即降序
    sortClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortClassCount[0][0]
  
if __name__ == "__main__": 
    train_x,train_y,test_x,test_y = main()
    startTime=datetime.datetime.now()
    testSize=test_x.shape[0]
    rightCount+=0
    for i in range(testSize):
        classifyResult=classifyKNN(test_x[i,:],train_x,train_y,3)
        if(classifyResult ==test_y[i]):
            rightCount+=1
    endTime=datetime.datetime.now()
    print 'use time: '+str(endTime-startTime)
    print 'right rate: '+str(rightCount*1.0/len(test_y))
    #    testKNN()
#    x=classifyKNN(test_x[0],train_x,train_y,3)

#    outImage()
#    print test_y
    #testKNN()
#    image=train_x.reshape(28,28)
#    fig=plt.figure()
#    plotwindow=fig.add_subplot(111)
#    plt.imshow(image,cmap='binary')
#    plt.show()