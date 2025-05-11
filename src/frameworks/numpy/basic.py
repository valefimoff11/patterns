import numpy as np

x = np.array([1, 2, 4, 7, 0])

#differencing
print(np.diff(x))

a = np.array([20, 30, 40, 50])
b = np.arange(4)

c = a - b
print(c)

print(b**2)

print(10 * np.sin(a))

print(a < 35)



A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])

print(A)
print(B)

print(A * B)     # elementwise product

print(A @ B)     # matrix product

print(A.dot(B))  # another matrix product
