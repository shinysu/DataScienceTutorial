import numpy as np

reshaped = np.arange(1, 10).reshape((3, 3))
print(reshaped)

x = np.array([1, 2, 3])
print(x)

# row vector via reshape
x_rv= x.reshape((1, 3))
print(x_rv)

# column vector via reshape
x_cv = x.reshape((3, 1))
print(x_cv)

# We can concatenate two or more arrays at once.
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [11,11,11]

np.concatenate([x, y, z])
#> array([ 1,  2,  3,  3,  2,  1, 11, 11, 11])

# We can also concatenate 2-dimensional arrays.
grid = np.array([[1,2,3] , [4,5,6]])
np.concatenate([grid, grid])
#> array([[1, 2, 3],
#>       [4, 5, 6],
#>       [1, 2, 3],
#>       [4, 5, 6]])


x = np.array([3,4,5])
grid = np.array([[1,2,3],[9,10,11]])

np.vstack([x,grid]) # vertically stack the arrays
#> array([[ 3,  4,  5],
#>       [ 1,  2,  3],
#>       [9, 10, 11]])

z = np.array([[19],[19]])
np.hstack([grid,z])  # horizontally stack the arrays
#> array([[ 1,  2,  3, 19],
#>       [9, 10, 11, 19]])


x = np.arange(10)
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x1, x2, x3 = np.split(x,[3,6])
print(x1, x2, x3)
#> [0 1 2] [3 4 5] [6 7 8 9]

grid = np.arange(16).reshape((4, 4))
print(grid, "\n")

# Split vertically and print upper and lower arrays
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower, "\n")

# Split horizontally and print left and right arrays
left, right = np.hsplit(grid, [2])
print(left)
print(right)