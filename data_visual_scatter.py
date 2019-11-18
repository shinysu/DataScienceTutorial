import numpy as np
import matplotlib.pyplot as plt
# 2. Generating some random data
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

# 3. Create a scatterplot using the a colormap.
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5,cmap='viridis')
plt.colorbar();  # To show the color scale

plt.savefig("scatter.png")
'''We can see that this scatter plot has given us the ability to simultaneously explore four different dimensions of the data. 
If this was a real data set, the x, y location of each point can be used to represent two distinct features. 
The size of the points can be used to represent a third feature, and the color mapping can be used to represent different 
classes or groups of the data points. '''

