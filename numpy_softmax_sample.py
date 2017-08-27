import numpy as np 

m = np.random.rand(10, 10) * 10 + 1000
print(m)

# 每一行转换成概率分布
m_row_max = m.max(axis=1).reshape(10, 1)
print(m_row_max, m_row_max.shape)

m = m - m_row_max
print(m)

m_exp = np.exp(m)
print(m_exp, m_exp.shape)

m_exp_row_sum = m_exp.sum(axis=1).reshape(10, 1)
print(m_exp_row_sum, m_exp_row_sum.shape)

m_softmax = m_exp / m_exp_row_sum
print(m_softmax)

print(m_softmax.sum(axis=1))
