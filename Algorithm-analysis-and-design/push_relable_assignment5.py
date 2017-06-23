# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:57:21 2016
@author: Jiao
"""
nodeNum, edgeNum = 6, 8  
s, t = -1, -1 
nodes = [-1] * nodeNum  
for i in range(s, t + 1):  
    nodes[i - s] = i  
flow_matrix = [[0 for i in range(nodeNum)] for j in range(nodeNum)]  
adjacent_matrix = [  #输入的邻接矩阵
[0,5,15,0,0,0],
[0,0,0,5,5,0],
[0,0,0,5,5,0],
[0,0,0,0,0,15],
[0,0,0,0,0,5],
[0,0,0,0,0,0]]
forward_matrix=adjacent_matrix

height = [0] * nodeNum  
height[0] = nodeNum  
for i in range(len(adjacent_matrix)):  
    flow_matrix[0][i] = adjacent_matrix[0][i]  
    adjacent_matrix[0][i] = 0  
    adjacent_matrix[i][0] = flow_matrix[0][i]  
def excess(v):  
    in_flow, out_flow = 0, 0  
    for i in range(len(flow_matrix)):  
        in_flow += flow_matrix[i][v]  
        out_flow += flow_matrix[v][i]  
    return in_flow - out_flow  
  
  
def exist_excess():  
    for v in range(len(flow_matrix)):  
        if excess(v) > 0 and v != t - s:  
            return v  
    return None  
  
flow=0 
v = exist_excess()  
while v:  
    has_lower_height = False  
    for j in range(len(adjacent_matrix)):  
        if adjacent_matrix[v][j] != 0 and height[v] > height[j]:  
            has_lower_height = True  
            if forward_matrix[v][j] != 0:  
                bottleneck = min([excess(v), adjacent_matrix[v][j]])  
                flow_matrix[v][j] += bottleneck  
                adjacent_matrix[v][j] -= bottleneck  
                adjacent_matrix[j][v] += bottleneck 
                flow=15
            else:  
                bottleneck = min([excess(v), flow_matrix[j][v]])  
                flow_matrix[j][v] -= bottleneck  
                adjacent_matrix[v][j] -= bottleneck  
                adjacent_matrix[j][v] += bottleneck            
    if not has_lower_height:  
        height[v] += 1  
    v = exist_excess()  
print "Max flow:",flow  #输出
