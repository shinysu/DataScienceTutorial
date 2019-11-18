# 1. Importing modules
import matplotlib.pyplot as plt

# 2. Getting the Data
year = [1970, 1980, 1990, 2000, 2010, 2020]
pop_A = [4.9, 5.3, 7.1, 10.7, 13.5, 15.6]
pop_B = [44.4, 55.6, 69.7, 87.1, 95.4, 100.5]

# 3. Visualising the Data
plt.plot(year, pop_A, color='g')
plt.plot(year, pop_B, color='r')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Populations over the years')

plt.savefig("line.png")

'''Say we have a dataset with the population of two cities over time and we want to see if there is some correlation in 
their population sizes. We can use the plt.plot() function to plot population against time. We would put time on the 
x-axis and population on the y-axis.'''
