i=j=[3]
print(id(i))
print(id(j))
i+=j
print(i,j)
#i=j=[3] is different from i=[3] and j=[3]
Tuplex=(65,65,"A")
#print(max(Tuplex)) -> it gives error
value =10
def func():
    value=20
    print(value,end=" ")
func()
print(value)