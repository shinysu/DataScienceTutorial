import numpy as np

x = np.arange(10)

# Native arithmentic operators
print("x =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 5 =", x * 5)
print("x / 5 =", x / 5)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)

# OR we can use explicit functions, ufuncs, e.g. "add" instead of "+"
print(np.add(x, 5))
print(np.subtract(x, 5))
print(np.multiply(x, 5))
print(np.divide(x, 5))
print(np.power(x, 2))
print(np.mod(x, 2))

theta = np.linspace(0, np.pi, 4)
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

x = [1, 2, 3]
print("x     =", x)
print("e^x   =", np.exp(x))
print("2^x   =", np.exp2(x))
print("3^x   =", np.power(3, x))

print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))

'''calling reduce on the add functions returns the sum of all elements in the array:'''

x = np.arange(1, 6)
sum_all = np.add.reduce(x)

print(x)
print(sum_all)

'''If we need to store all the intermediate results of the computation, we can use accumulate() instead:'''
x = np.arange(1, 6)
sum_acc = np.add.accumulate(x)

print(x)
print(sum_acc)