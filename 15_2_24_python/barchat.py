import matplotlib.pyplot as plt
import numpy as np

python=(22,45,67)
java=(12,67,45,)
js=(99,89,98)

persons=["a","b","c"]
index=np.arange(3)
plt.bar(index,python,width=0.3,)
plt.bar(index+0.3,java,width=0.3)
plt.bar(index+0.6,js,width=0.3)
plt.title("marks of pros")
plt.xlabel="people"
plt.ylabel="marks"
plt.xticks(index+0.3,persons)
plt.ylim(0,100)
plt.show()