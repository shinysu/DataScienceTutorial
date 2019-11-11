import numpy as np

x = np.array([1, 2, 3, 4, 5])

print(x < 2) # less than
print(x >= 4) # greater than or equal

x = np.array([1, 2, 3, 4, 5])

# Elements for which multiplying by two is the same as the square of the value
(2 * x) == (x ** 2)
#> array([False,  True, False, False, False], dtype=bool)

x = np.arange(10)
print(x)

# How many values less than 6?
print(np.count_nonzero(x < 6))

# Are there any values greater than 8?
print(np.any(x > 8))

# Are all values less than 10?
print(np.all(x < 10))

# Random integers between [0, 10) of shape 3x3
x = np.random.randint(0, 10, (3, 3))
print(x)

# Boolean array
print(x < 6)

# Boolean mask
print(x[x < 6])

