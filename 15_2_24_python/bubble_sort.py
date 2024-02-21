arr = [23, 14, 64, 13, 64, 23, 86]  
def bub(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
print(arr)   
bub(arr)
print(arr)             