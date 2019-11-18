'''A histogram represents the frequency distribution of continuous variables while a bar graph is a diagrammatic comparison
of discrete variables. The histogram presents numerical data whereas the bar graph shows categorical data. The histogram
is drawn in such a way that there is no gap between the bars.'''

import numpy as np
import matplotlib.pyplot as plt

# Input data
labels = ('Python', 'C++', 'Java', 'Perl', 'C#')
num_users = [12,8,15,4,6]
'''To make a bar plot from this data, we first need to convert the labels from string data into numerical data that be 
used for plotting purposes.'''
'''We can use NumPy’s arange method to generate an array of sequential numbers of the same length as the labels array like this:'''
index = np.arange(len(labels))


# Plotting
plt.bar(index, num_users, align='center', alpha=0.5)
plt.xticks(index, labels)
plt.xlabel('Language')
plt.ylabel('Num of Users')
plt.title('Programming language usage')

plt.savefig('barplot.png')