import numpy as np


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

x+y  # 逐元素求和
np.add(x,y)  # 另一种逐元素求和

x-y  # 逐元素做差
np.subtract(x,y)  # 另一种逐元素做差

x*y  # 逐元素相乘
np.multiply(x,y)  # 另一种逐元素相乘

x/y
np.divide(x, y)

np.sqrt(x)  # 逐元素做平方根


# matrix multiplication
v = np.array([9,10])
w = np.array([10,11])
print(v.shape)  # (2,)
print(v.dot(w))  # 求向量内积
print(np.dot(v,w))  # 求向量内积

x = np.array([[1,2], [3,4]])
print(x.T)  # 转置

arr = np.arange(16).reshape(2,2,4)  # 高维转置
print(arr, arr.shape)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]] (2, 2, 4)
'''
print(arr.transpose((1,0,2)))
'''
[[[ 0  1  2  3]
  [ 8  9 10 11]]

 [[ 4  5  6  7]
  [12 13 14 15]]]
'''
print(arr.transpose((0,2,1)))
'''
[[[ 0  4]
  [ 1  5]
  [ 2  6]
  [ 3  7]]

 [[ 8 12]
  [ 9 13]
  [10 14]
  [11 15]]]
'''


x= np.array([[1,2], [3,4]])
print(np.sum(x))
print(x.sum())  # 矩阵内求和
print(np.sum(x, axis=0))  # [4 6]
print(np.mean(x))
print(np.mean(x, axis=0))
print(np.mean(x, axis=1))  # 平均数
print(x.cumsum(axis=0))
print(x.cumsum(axis=1))  # 每一行的累积和
print(x.cumprod(axis=0))
print(x.cumprod(axis=1)) 


# 一维数组的排序
arr = np.random.randn(8) * 10
print(arr)
arr.sort()
print(arr)
# 二维数组也可以在某些维度上排序
arr = np.random.randn(5,3) * 10
print(arr)
arr.sort(1)
print(arr)
# 找出排序后位置在5%的数字
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])
