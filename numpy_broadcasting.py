import numpy as np 


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
print(x)
print()
print(v)

# 给x的每一行都逐元素加上一个向量，然后生成y
y = np.empty_like(x)
print(y)

# 比较粗暴的方式是，用for循环逐个相加
for i in range(4):
    y[i,:] = x[i,:] + v
    
print(y)

# Numpy broadcasting allows us to perform this computation without actually creating multiple copies of v. Consider this version, using broadcasting:
print(x.shape, v.shape)
print(x + v)
'''
(4, 3) (3,)
array([[ 2,  2,  4],
       [ 5,  5,  7],
       [ 8,  8, 10],
       [11, 11, 13]])
'''
'''
当操作两个array时，numpy会逐个比较它们的shape，在下述情况下，两arrays会兼容和输出broadcasting结果：
  相等
  其中一个为1，（进而可进行拷贝拓展已至，shape匹配）

e.g.
  Image (3d array):  256 x 256 x 3
  Scale (1d array):              3
  Result (3d array): 256 x 256 x 3

  A      (4d array):  8 x 1 x 6 x 1
  B      (3d array):      7 x 1 x 5
  Result (4d array):  8 x 7 x 6 x 5

  A      (2d array):  5 x 4
  B      (1d array):      1
  Result (2d array):  5 x 4

  A      (2d array):  15 x 3 x 5
  B      (1d array):  15 x 1 x 5
  Result (2d array):  15 x 3 x 5
'''
v = np.array([1,2,3])
w = np.array([4,5])
print(v.shape, w.shape)  # (3,) (2,)
v = v.reshape(3,1)
print(v.shape)  # (3, 1)
print(v + w)
'''
array([[5, 6],
       [6, 7],
       [7, 8]])
'''
 
