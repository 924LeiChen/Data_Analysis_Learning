import numpy as np 


# 读取csv文件作为数组
arr = np.loadtxt('arraytest.txt', delimiter=',')
print(arr)
# 数组文件读写
arr = np.arange(50).reshape(2,5,5)
print(arr)
np.save('test_array', arr)
arr2 = np.load('test_array.npy')
print(arr2)
arr3 = np.arange(15).reshape(3,5)
# 多个数组可以一起压缩存储
np.savez("array_test01.npz", arr=arr, b=arr2, c=arr3)
arch = np.load('array_test01.npz')
print(arch['arr'])
print(arch['b'])
print(arch['c'])
