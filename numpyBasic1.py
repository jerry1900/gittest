#-*-coding:utf8-*-
__author__ = 'jerry1900'

import numpy as np
#
#  np 矩阵的创建、属性
#

#将列表转化为矩阵
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#查看维度
print('num of dim:',a.ndim)

#查看shape
print('shape:',a.shape)

#查看元素个数
print('size:',a.size)

#指定数据 dtype
a = np.array([[1,2],[3,4]],dtype = np.float64)
print(a.dtype)
a = np.array([[1,2],[3,4]],dtype = np.int16)
print(a.dtype)

#创建全零数组
a = np.zeros((3,4))
print a

#创建连续数组
a = np.arange(0,20,1)
print a

#改变数据的形状
a = np.arange(15).reshape(3,5)
print a

#用linspace创建线段型数组
a = np.linspace(0,10,100).reshape(5,20)
print a.size,a.dtype,a.shape

#用 -1 作为shape的占位符
print a.shape
a.shape = (10,-1)
print a.shape

