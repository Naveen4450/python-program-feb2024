import numpy as np
import matplotlib.pyplot as plt
m,s=172,8
x=m+s*np.random.randn(1000)
plt.hist(x,100,density=True)
plt.show()