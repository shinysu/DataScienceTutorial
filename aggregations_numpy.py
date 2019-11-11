import numpy as np

x = np.random.random(100)

# Sum of all the values
print("Sum of values is:", np.add.reduce(x))
# Mean value
print("Mean value is: ", np.mean(x))

#For min, max, sum, and several other NumPy aggregates,
#a shorter syntax is to use methods of the array object itself,
# i.e. instead of np.sum(x), we can use x.sum()
print("Sum of values is:", x.sum())
print("Mean value is: ", x.mean())
print("Max value is: ", x.max())
print("Min value is: ", x.min())

'''if we want to compute the minimum row wise or column wise, we can use the np.amin version instead. '''
grid = np.random.random((3, 4))
print(grid)

print("Overall sum:", grid.sum())
print("Overall Min:", grid.min())

# Row wise and column wise min
print("Column wise minimum: ", np.amin(grid, axis=0))
print("Row wise minimum: ", np.amin(grid, axis=1))

