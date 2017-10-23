#normal distribution from binomial distribution

from scipy.stats import binom
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(1,1)
x = [0,1,2,3,4,5,6,7]
n, p = 2, 0.4
rv = binom(n,p)
ax.vlines(x, 0, rv.pmf(x), colors = 'k', linestyles = '-', lw = 1, label = 'probability')
ax.legend(loc= 'best', frameon = False)
plt.show()