# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:35:57 2016

@author: Jiao
""" 
import struct

CodeDict={}
encodeDict={}
filename=None
ListEveryByte=[]
#清空树
class Node:
    def __init__(self,freq=0,charcode=None):
        self.left=None
        self.right=None
        self.father=None
        self.freq=freq
        self.charcode=charcode
    def Left(self):
        return self.father.left==self
 #创建叶子结点       
def CreateNodes(freqs):
    return [Node(freq)for freq in freqs]
              
#创建Huffman树
#得到根节点
def CreateHuffman_Tree(nodes):
    queue=nodes[:]
    while len(queue)>1:
        queue.sort(key=lambda item:item.freq)#排序
        node_left=queue.pop(0)
        node_right=queue.pop(0) #取出频率最小两个字符，分别为二叉树的左右节点
        node_father =Node(node_left.freq+node_right.freq)
        node_father.left=node_left #两个子节点的频率和为父节点
        node_father.right=node_right
        node_left.father=node_father
        node_right.father=node_father
        queue.append(node_father)
    queue[0].father=None
    return queue[0]  
#读取文件    
def ReadFile():
    global CodeDict
#    filename=raw_input("input file name:")
    global filename
    global listForEveryByte
#    filename="Aesop_Fables.txt"
    filename="graph.txt"
    with open(filename,'rb')as f:
        data=f.read()
    for Byte in data:
        CodeDict.setdefault(Byte,0)
        CodeDict[Byte]+=1
        ListEveryByte.append(Byte)
def OutputFile():
    global ListEveryByte
    fileString=""
    with open((filename.split(".")[0]+"_comparessed.bin"),"wb") as f:
        for Byte in ListEveryByte:
            fileString+=encodeDict[Byte]
        lens=len(fileString)
        more=16-lens%16
        fileString =fileString+"0"*more  
        lens=len(fileString)
        i,j=0,16
        while j<=lens:
            k=fileString[i:j]
            a=int(k,2)
            f.write(struct.pack(">H",a))
            i=i+16
            j=j+16
            
def DecompressFile():
    with open((filename.split(".")[0]+"_comparessed.bin"),"rb") as f:
        all_data = f.read()
        i,j=0,2
        lens = len(all_data)
        s=[]
        while j < lens:
            k = all_data[i:j]
            s.append(struct.unpack(">H",k))
            print k
            i += 2
            j += 2
        return s
 #Huffman编码
#从根结点到每个叶子结点的路径，就是该字符的前缀编码
def HuffmanEncoding(root,nodes):
    global encodeDict
    for i in range(len(nodes)):
        e=nodes[i]  #不清楚怎么处理
        ep = e
        encodeDict.setdefault(e.charcode,"")
        while ep!=root:
            if ep.father.left==ep:
                encodeDict[e.charcode]="1"+encodeDict[e.charcode]
            else:
                encodeDict[e.charcode]="0"+encodeDict[e.charcode]
            ep=ep.father


if __name__=='__main__':
    ReadFile()
    nodes=[]
    for e in CodeDict.keys():
        nodes.append(Node(freq=CodeDict[e],charcode=e))
    root=CreateHuffman_Tree(nodes)
    HuffmanEncoding(root,nodes)
    OutputFile()
    s = DecompressFile()
#    with open((filename.split(".")[0]+"_comparessed.bin"),"rb") as f:
#        all_data = f.read()
    for i in encodeDict.keys():
        print(i,encodeDict[i])
#    for index in zip(chars_freqs,codes):
#        print

 
    