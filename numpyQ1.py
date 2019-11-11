'''Create a null vector (all zeros) of size 10 and set it in the variable called “Z”.'''

import numpy as np
z= np.zeros(10)
print(z)


'''Q2. Create a 1D array of numbers from 0 to 9 and set it in the variable called “arr”.'''

arr = np.arange(10)
#print(arr)


'''Q3. Create a 3x3x3 array with random values and set it in the variable called “arr”.'''

arr= np.random.random(size=(3, 3, 3))
#print(arr)

'''Q4.Create a 10x10 array with random values called “arr4”. 
Find its minimum and maximum values and set them in the variables called “min_val” and “max_val” respectively.'''

arr4 = np.random.random((10,10))
min_val = arr4.min()
max_val = arr4.max()


'''First create a 1D array with numbers from 1 to 9 and then convert it into a 3x3 grid. Store the final answer in the 
variable called “grid”.'''
arr=np.arange(1,10)
print(arr)
grid = np.reshape(arr,(3,3))
print(grid)
# grid = np.arange(1, 10).reshape((3, 3))

'''Q6. Replace the maximum value in the given vector, “arr6”, with -1.'''
# Input
arr6 = np.arange(10)
arr6[arr6.argmax()] = -1 #Use arr6.argmax() to find the index of the max value

'''Q7. Reverse the rows of the given 2D array, “arr7”.'''
arr7 = np.arange(9).reshape(3,3)
arr7 = arr7[::-1,]

'''Q8. Subtract the mean of each row of the given 2D array, “arr8”, from the values in the array. 
Set the updated array in “transformed_arr8”.'''
arr8 = np.random.rand(3, 10)
transformed_arr8 = arr8 - arr8.mean(axis=1, keepdims=True)