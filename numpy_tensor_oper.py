import numpy as np 


x_arr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
print(np.where(cond, x_arr, y_arr))  # [ 1.1  2.2  1.3  1.4  2.5]
arr = np.random.rand(4, 4)
print(arr)
'''
[[ 0.94534017  0.04955986  0.20184702  0.40272432]
 [-0.20872753 -0.04952711  0.0059752  -1.9356753 ]
 [ 1.20042485 -0.92834374  1.57810979 -0.96378859]
 [-2.09492281 -0.38678213 -0.67656147  1.45629059]]
'''
print(arr > 0)
'''
array([[ True,  True,  True,  True],
       [False, False,  True, False],
       [ True, False,  True, False],
       [False, False, False,  True]], dtype=bool)
'''
print(np.where(arr > 0, 1,-1))
'''
[[ 1  1  1  1]
 [-1 -1  1 -1]
 [ 1 -1  1 -1]
 [-1 -1 -1  1]]
'''
print(np.where(arr > 0, 1,arr))
'''
[[ 1.          1.          1.          1.        ]
 [-0.20872753 -0.04952711  1.         -1.9356753 ]
 [ 1.         -0.92834374  1.         -0.96378859]
 [-2.09492281 -0.38678213 -0.67656147  1.        ]]
'''


# 使用reshape来改变tensor的形状
arr = np.arange(8)
print(arr.shape)  # (8,)
arr.reshape(2,4)
arr.reshape(2,2,2)
arr = np.arange(15)
print(arr.reshape(5,3).shape)
print(arr.reshape(5,-1).shape)  # 如果我们在某一个维度上写上-1，numpy会帮我们自动推导出正确的维度

# 还可以从其他的ndarray中获取shape信息然后reshape
other_arr = np.ones((3,5))
print(other_arr.shape) # tuple
arr.reshape(other_arr.shape)
'''
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
'''
# 高维数组可以用ravel来拉平
arr = arr.reshape(other_arr.shape)
print(arr)
print(arr.ravel().shape)  # (15,)


# 连接两个二维数组
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
np.concatenate([arr1, arr2], axis=0)
'''
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
'''
np.concatenate([arr1, arr2], axis=1)
'''
array([[ 1,  2,  3,  7,  8,  9],
       [ 4,  5,  6, 10, 11, 12]])
'''
# 堆叠
np.vstack((arr1, arr2)) # vertical
np.hstack((arr1, arr2)) # horizontal
# 拆分数组
arr = np.random.rand(5,5)
print(arr)
'''
[[ 0.26127473  0.32154252  0.77145446  0.96708767  0.73012212]
 [ 0.07292513  0.44467037  0.37541603  0.05989568  0.77563346]
 [ 0.47542526  0.15934487  0.72384244  0.69574257  0.74326743]
 [ 0.64811628  0.22862968  0.14491565  0.83034272  0.44879975]
 [ 0.77389528  0.14592582  0.65473048  0.44917534  0.21280217]]
'''
print('\n\n\n')
first, second, third = np.split(arr, [1,3], axis=0)
print(first, '\n\n', second, '\n\n', third)
'''
[[ 0.27896389  0.22192585  0.23071216  0.78324018  0.59262444]] 

 [[ 0.81119576  0.78253094  0.62041785  0.33052932  0.24629957]
 [ 0.65744424  0.27400006  0.8935538   0.94779115  0.29764111]] 

 [[  5.27532920e-01   9.55858973e-01   7.41791105e-02   4.40641789e-01
    7.72783001e-01]
 [  5.35936323e-01   8.95425504e-01   3.83907231e-01   3.36982823e-04
    5.99817796e-01]]
'''

# 堆叠辅助
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print(arr1)
print(arr2)
# r_用于按行堆叠
print(np.r_[arr1, arr2])
print()
# c_用于按列堆叠
print(np.c_[np.r_[arr1, arr2], arr])
print()
# 切片直接转为数组
np.c_[1:6, -5:0]
# 使用repeat来重复
arr = np.arange(3)  # [0 1 2]
print(arr.repeat(3))  # [0 0 0 1 1 1 2 2 2]
print(arr.repeat([2,3,5]))  # [0 0 1 1 1 2 2 2 2 2]
# 指定axis来重复
arr = np.random.rand(2,2)
print(arr)
print(arr.repeat(2, axis=0))
print(arr.repeat(2, axis=1))
print(np.tile(arr, 2))
print(np.tile(arr, (2,3)))
