# numpy is used for creating fake data
import numpy as np
import matplotlib.pyplot as plt

# Create data
data_group1 = np.random.normal(100, 10, 200)
data_group2 = np.random.normal(80, 30, 200)
data_group3 = np.random.normal(90, 20, 200)

# combine these different datasets into a list
data_to_plot = [data_group1, data_group2, data_group3]

# Create the boxplot
# patch_artist must be True to control box fill (color-filled boxes)
plt.boxplot(data_to_plot, patch_artist = True)

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Some Group Scores')

# Save the figure
plt.savefig('boxplot.png')