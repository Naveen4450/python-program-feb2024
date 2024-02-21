import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,100,1)
y1=np.sin(x)
y2=x**2 + 2*x
plt.figure(1)
ax1=plt.subplot(121)
ax2=plt.subplot(122)
ax1.plot(x,y1,"r-")
ax2.plot(x,y2,"g.")
plt.tight_layout()
plt.show()