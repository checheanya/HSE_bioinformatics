import numpy as np
from scipy.stats import uniform
import math

a1 = 0
b1 = math.exp(1/3)
rv1 = uniform(a1, b1)
x2 = rv1.rvs(size=10000)
f1 = 27*(x2*(np.log(x2)))**2
print((np.mean(f1))*(b1-a1))
