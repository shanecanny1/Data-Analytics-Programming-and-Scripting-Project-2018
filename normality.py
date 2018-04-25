
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.genfromtxt('irisdata/iris.csv',delimiter=',')
SetosadataSepallength = data[0:50:,0]
SetosadataSepalwidth = data[0:50:,1] 
SetosadataPetallength = data[0:50:,2] 
SetosadataPetalwidth = data[0:50:,3]


k2, p = stats.normaltest(SetosadataSepallength)
alpha = 5e-2 # Setting the confidence level for alpha at 95%
print("p = {:g}".format(p))
if p < alpha:  # null hypothesis: the data SetosadataSepallength follows the normal distribution
     print("We can reject the null hypothesis for SetosadataSepallength the data does not follows the normal distribution")
else:
     print("We can fail to reject the null hypothesis for SetosadataSepallength the data follows the normal distribution")

k2, p = stats.normaltest(SetosadataSepalwidth)
alpha = 5e-2 # Setting the confidence level for alpha at 95%
print("p = {:g}".format(p))
if p < alpha:  # null hypothesis: the data SetosadataSepalwidth follows the normal distribution
     print("We can reject the null hypothesis for SetosadataSepalwidth the data does not follows the normal distribution")
else:
     print("We can fail to reject the null hypothesis for SetosadataSepalwidth the data follows the normal distribution")

k2, p = stats.normaltest(SetosadataPetallength)
alpha = 5e-2 # Setting the confidence level for alpha at 95%
print("p = {:g}".format(p))
if p < alpha:  # null hypothesis: the data SetosadataPetallength follows the normal distribution
     print("We can reject the null hypothesis for SetosadataPetallength the data does not follows the normal distribution")
else:
     print("We can fail to reject the null hypothesis for SetosadataPetallength the data follows the normal distribution")

k2, p = stats.normaltest(SetosadataPetalwidth)
alpha = 5e-2 # Setting the confidence level for alpha at 95%
print("p = {:g}".format(p))
if p < alpha:  # null hypothesis: the data SetosadataPetalwidth follows the normal distribution
     print("We can reject the null hypothesis for SetosadataPetalwidth the data does not follows the normal distribution")
else:
     print("We can fail to reject the null hypothesis for SetosadataPetalwidth the data follows the normal distribution")

# Test for Generating

plt.hist(SetosadataSepallength)
plt.title("Sepal Length")
plt.xlabel("Length")
plt.ylabel("Qty")
plt.savefig("SetosadataSepallength.png")


