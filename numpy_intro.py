import numpy as np


# 调用np.array去从list初始化一个数组 
a = np.array([1, 2, 3])
print(a)
print(type(a))  # <class 'numpy.ndarray'>
b = np.array([[1, 2, 3], [2, 3, 4]])  # 二维array
print(b)
print(b.shape)  #（2， 3）


# 内置创建函数的数组
a = np.zeros((2,3))
print(a)
b = np.ones((1,2))
print(b)
c = np.full((2,2), 8)
print(c)
d = np.eye(3)
print(d)
e = np.random.random((3,2))  # 0 - 1
print(e)
f = np.empty((2,3,4))  #uninitialized
print(f)
g = np.arange(15)  # 0 - 14
print(g)
print(g.shape)  #(15,)


# 数组可以有不同类型
arr = np.array([1,2,3])
print(arr.dtype)  # int32
arr = np.array([1,2,3], dtype=np.float64)
print(arr.dtype)  # float64
# 生成数组时可以指定数据类型，如果不指定numpy会自动匹配合适的类型

# 使用astype复制数组并转换数据类型
int_arr = np.array([1,2,3,4,5])
print(int_arr, int_arr.dtype)
float_arr = int_arr.astype(np.float64)
print(float_arr.dtype, float_arr)  # float64 [ 1.  2.  3.  4.  5.]
# 使用astype将float转换为int时小数部分被舍弃
# 使用astype把字符串转换为数组，如果失败抛出异常。


