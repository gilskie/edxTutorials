import numpy as np

# ax = np.array([1,2,3,4,5])
# print(f"{ax}, {id(ax)}, {len(ax)}")
#
# x = ['1', '2', '3']
# xi = np.array(x, 'int')
# xf = np.array(x, 'float')
# xs = np.array(x, 'str')
#
# print(f"{xi} - {type(xi)} \r\n{xf} - {type(xf)} \r\n{xs} - {type(xs)}")

# y = ['1.3', '2.22', '3.56']
# yf = np.array(y, 'float')
# print(f"sum={yf.sum()}, mean={yf.mean()}, standard deviation={yf.std()}")

# multi dimensional

# x = [[0,1,2,3,4,5], [6,7,8,9,10,11], [12,13,14,15,16,17]]
# xs = np.array(x, str)
# xf = np.array(x, float)
# print(xf)

# indexing
# print(f"{xf[1,4]}")

# slicing
# print(f"{xf[1:3, 2:4]}")

# get shaping
#print(xf.shape)

# reshaping
# print(xf.reshape(9,2))

# initializing array
# ax = np.arange(10)
# print(f"{ax}")
#
# ay = np.array([np.arange(10), np.arange(10)])
# print(f"\r\n{ay}")

# ax = np.ones(10, 'str')
# print(f"{ax}")

# ax = np.arange(10)**2
# print(ax)

# ax = np.identity(10)
# print(f"{ax}")

# ax = np.arange(10)
# ay = np.array([ax, ax])
# print(f"{ay*2}")
#
# print(f"{ay.shape}")

x = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
ax = np.array(x, float)

print(f"{ax}\r\n\r\n{np.where(ax % 2 ==0, 'divisible', 'not divisible')}")