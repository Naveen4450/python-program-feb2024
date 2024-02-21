n=int(input("enter the value of n"))
l=[]
for i in range(n):
    x=int(input("enter the element"))
    l.append(x)
print(l)
c=sum(l)/n
print("the mean of elements is",c)

