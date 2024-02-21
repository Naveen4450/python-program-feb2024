n=int(input("enter the number"))
num=0
while (n!=0):
    x=n%10
    num=num*10+x
    n=n//10
print(num)
    
    