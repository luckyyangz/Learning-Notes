# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:36:43 2016

@author: Jiao
"""

import struct
import numpy as np
import matplotlib.pyplot as plt
#import os
class Mnist_import(object):
    def __init__(self,filename=None,outpath=None):
        self._filename=filename
        self._outpath=outpath
        self._tag='>'
        self._4Bytes='IIII'
        self._2Bytes='II'
        self._pictureBytes='784B'
        self._labelByte='1B'
        self._4Bytes2=self._tag+self._4Bytes
        self._2Bytes2=self._tag+self._2Bytes
        self._labelByte2=self._tag+self._labelByte
        
    def getImage(self):
        """将MNIST的birary文件转换成像素特征数据"""
        binfile=open(self._filename,'rb')
        buf=binfile.read()
        binfile.close() #为什么关闭文件
        index=0   #'IIII'使用大端法读取4个unsingen int32
        magic,numImages,numRows,numColumns=struct.unpack_from('>IIII',buf,index)   
        index+=struct.calcsize('>IIII')
        
        images=[]
        #for i in range(numImages):
        for i in range(1000):
            imgVal=struct.unpack_from('>784B',buf,index)
            index+=struct.calcsize('>784B')
            imgVal=list(imgVal)
            for j in range(len(imgVal)):
                if imgVal[j]>1:
                    imgVal[j]=1
            images.append(imgVal)
        return np.array(images)
        
    def getLabel(self):
        """将MNIST中的label二进制文件转换成对应的label数字特征"""
        binfile=open(self._filename,'rb')
        buf=binfile.read()
        binfile.close()
        index=0
        magic,numItems=struct.unpack_from(self._2Bytes2,buf,index)
        index+=struct.calcsize(self._2Bytes)
        labels=[]
       # for x in range(numItems):
        for x in range(1000):
            im=struct.unpack_from(self._labelByte2,buf,index)
            index +=struct.calcsize(self._labelByte2)
            labels.append(im) #方法向列表的尾部添加一个新的元素。只接受一个参数。
        return np.array(labels)  
    def outImage(self,arrX,arrY):
        """根据生成的特征和数字标号，输出png图像"""
        m,n=np.shape(arrX)
        for i in range(1):
            img=np.array(arrX[i])
            img=img.reshape(28,28)
            outfile=str(i)+"_"+str(arrY[i])+".png"
            plt.imshow(img,cmap='binary')
            plt.savefig(self._outpath+"/"+outfile)
        
        