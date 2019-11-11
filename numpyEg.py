import numpy as np
arr1 = np.array([1, 2, 3, 4],dtype='float')
print(arr1)
print(arr1 * 2)
print(arr1 * arr1)
print(type(arr1))

#create an integer array of length 100 filled with zeroes
arr2 = np.zeros(100, dtype=int)
#print(arr2)

#create a 3*3 floating point array filled with ones
arr3 = np.ones((3,3),dtype=float)
print(arr3)

#create an array filled with a linear sequence
#starting at 0, ending at 20, stepping by 3
arr4=np.arange(0,20,3)
#print(arr4)

#create an array of 100 values evenly spaced between 0 and 1
arr5=np.linspace(0,1,100)
#print(arr5)


#create a 3*3 array  of uniformly distributed ramdom variables between 0 and 1
a6= np.random.random((3,3))
print(a6)

# Create a 3x3 array of random integers in the interval [0, 10)
x = np.random.randint(0,10,(3,3))
print(x)
print("ndim: ", x.ndim)
print("shape:", x.shape)
print("x size: ", x.size)
print("dtype:", x.dtype)
print("itemsize:", x.itemsize, "bytes")
print("nbytes:", x.nbytes, "bytes")


# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
a8=np.random.normal(0, 1, (3, 3))
print(a8)

print(np.random.randint(10, size=6))  # One-dimensional array of random integers
print(np.random.randint(10, size=(3, 3)) ) # Two-dimensional array of random integers
print(np.random.randint(10, size=(3, 3, 3)))  # Three-dimensional array of random integers
