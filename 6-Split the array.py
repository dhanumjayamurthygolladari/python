def splitarr(a,n,k):
    b = a[:k]
    return(a[k::]+b[::])
arr=[14,23,28,32,31,31]
n=len(arr)
position=2
arr=splitarr(arr,n,position)
for i in range(0,n):
    print(arr[i],end=' ')
