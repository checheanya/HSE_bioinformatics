import numpy as np
from scipy.stats import uniform
import math

'''
rv = uniform(0,2)
a = 0
b = 2
x = rv.rvs(size=10000)
f = (x**2)*np.sqrt(4-x**2)
print((np.mean(f))*(b-a))
'''

rv = uniform(0,1)
x = rv.rvs(size=10000)
f = np.sinh(x) + np.cosh(x) + 1
print(np.mean(f))

