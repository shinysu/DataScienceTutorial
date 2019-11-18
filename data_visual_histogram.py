'''We can plot histograms using the hist() function:'''

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(x=data);

plt.savefig("hist1.png")

'''a more customized histogram for the same data:'''

plt.hist(data, bins=30, density=True, alpha=0.5,
                histtype='stepfilled', color='steelblue',
                edgecolor='none');

plt.savefig("hist2.png")

'''To create multiple histograms in the same plot, we can either call the hist() function multiple times or pass all the 
input values to it at once. The x parameter of hist() can take both a single array or a sequence of arrays as input.'''