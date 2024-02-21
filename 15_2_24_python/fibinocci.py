f=0
s=1
fib=[f,s]
n=int(input("enter no of series needed"))
for i in range(0,n-2):
    num=fib[i]+fib[i+1]
    fib.append(num)
    
print(fib)
