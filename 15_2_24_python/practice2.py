fruits = ["apple", "banana", "cherry", "kiwi", "mango","apple"]
#[a,b,c,d,e]=fruits
#print(a)
new=[]
for i in fruits:
    if "a" in i:
        new.append(i)
print(new)
new=set(new)
print(new)
new=list(new)
print(new)
x="hello world"
import re
y=re.sub("world","Naveen",x)
print(y)