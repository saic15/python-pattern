def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return(arr)
a=[3,4,5,8,6,7]
print(bubblesort(a))