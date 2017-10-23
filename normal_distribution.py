#normal distribution from binomial distribution

#if the coin is flipped 6 times, then getting three heads has 
#the maximum probability, whereas getting a single head or five head
#has the least probability.
#here we are increasing the number of attempts then the 
#distribution will be like this:
from scipy.stats import binom
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(1,1)
x = range(101)
n, p = 100, 0.5
rv = binom(n,p)
ax.vlines(x, 0, rv.pmf(x), colors = 'k', linestyles = '-', lw = 1, label = 'probability')
ax.legend(loc= 'best', frameon = False)
plt.show()