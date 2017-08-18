import numpy as np



a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
print(a.shape)

# 可以像list一样切片（多维数组可以从各个维度同时切片）
b = a[0:2,2:4].copy()
print(b)
# 可以修改切片出来的对象，然后完成对原数组的赋值.

row_r1 = a[1,:]
print(row_r1, row_r1.shape)  # [5 6 7 8] (4,)

row_r2 = a[1:2, :]
print(row_r2, row_r2.shape)  # [[5 6 7 8]] (1, 4)

row_r3 = a[[1], :]
print(row_r3, row_r3.shape)  # [[5 6 7 8]] (1, 4)

print(a)
'''
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
'''
col_r1 = a[:, 1]
print(col_r1, col_r1.shape)  # [ 2  6 10] (3,)

col_r2 = a[:, 1:2]
print(col_r2, col_r2.shape)
'''
[[ 2]
 [ 6]
 [10]] (3, 1)
'''

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)
'''
[[1 2]
 [3 4]
 [5 6]]
'''

print(a[[0,1,2], [0,1,0]])  # [1 4 5]
print(a[[0,1,2], [0,1,0]].shape)  # (3,)
print(np.array([a[0,0], a[1,1], a[2,0]]))  # [1 4 5]


a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
b = np.array([0, 2,0,1])  #下标
print(a[np.arange(4), b])  #array([ 1,  6,  7, 11])
a[np.arange(4), b] += 10
print(a)


a = np.array([[1,2], [3, 4], [5, 6]])
print(a)
bool_index = (a > 2)
print(bool_index)
'''
[[False False]
 [ True  True]
 [ True  True]]
'''
# 用刚才的布尔型数组作为下标就可以去除符合条件的元素
print(a[bool_index].shape)  # (4,)
print(a[a>2])  # [3 4 5 6]
