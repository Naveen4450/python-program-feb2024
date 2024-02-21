a="all"
b="all"
#print(a is b)
num=5
#s1={1,2}
#s2={3,4}
#s=s1+s2
#print(s)
#a=(65,64,"a")
#print(max(a))
a=[[]]*3
a[1].append(7)
#print(a)
string="python"
#print(string.find("py"))
a="naveen"
#print(a[::-1]) 
a="1234"
a=list(a)
a[0]=a[1]=5
#print(a)
a=[1]
b=[2]
print(a+b)
import numpy as np
a=np.array([1])
b=np.array([2])
print(a+b)
a=np.zeros((5,7,3))
b=np.full((5,7,3),9)
print(b)
p=np.random.random((5,10))
print(p)
a=np.array([[1,3],[3,5]])
for x in a.flat:
    print(x)

