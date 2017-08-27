import pandas as pd 
import numpy as np 


# Series是一个一维的数据结构
s = pd.Series([7, 'Beijing', 2.17, -1232, 'Happy birthday!'])
print(s)


# pandas会默认用0到n来作为Series的index，但是我们也可以自己指定index。
s = pd.Series([7, 'Beijing', 2.17, -1232, 'Happy birthday!'], 
                    index=['A', 'B', 'C', 'D', 'E'])
type(s)

# 还可以用dictionary来构造一个Series，因为Series本来就是key value pairs。
cities = {'Beijing': 55000, 'Shanghai': 60000, 'Shenzhen': 50000, 'Hangzhou':20000, \
         'Guangzhou': 25000, 'Suzhou': None}
apts = pd.Series(cities)
print(apts)
print(type(apts))

print(apts['Hangzhou'])
print(apts[["Hangzhou", "Beijing", "Shenzhen"]])
print(apts[apts < 50000])
less_than_50000 = apts < 50000
print(less_than_50000)  # there would be boolean type of all element
print(apts[less_than_50000])

# Series的元素可以被赋值
apts['Shenzhen'] = 55000
apts[apts <= 50000] = 40000
print(apts)

# basic math operation
apts / 2
apts * 2
print(np.square(apts))
# square也可以写成 **
apts ** 2


cars = pd.Series({'Beijing': 300000, 'Shanghai': 400000, 'Shenzhen': 300000, \
                      'Tianjin': 200000, 'Guangzhou': 200000, 'Chongqing': 150000})
print(cars)
print(cars + apts * 100)

# 数据缺失
print('Hangzhou' in apts)  # True
print(apts.notnull())
'''
Beijing       True
Guangzhou     True
Hangzhou      True
Shanghai      True
Shenzhen      True
Suzhou       False
dtype: bool
'''
print(apts.isnull())  # just the opposite
apts[apts.isnull()]  # Suzhou   NaN
print(apts[apts.isnull() == False])
'''
Beijing      55000.0
Guangzhou    40000.0
Hangzhou     40000.0
Shanghai     60000.0
Shenzhen     55000.0
dtype: float64
'''

