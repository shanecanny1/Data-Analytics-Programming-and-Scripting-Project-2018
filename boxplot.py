# Testing Boxplots
# Copied from http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/

import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt


np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]
petal = plt.figure(1, figsize=(9, 6))
plt.boxplot(data_to_plot)
petal.savefig('petallenght1.png')



