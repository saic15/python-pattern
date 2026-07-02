def quicksort(arr):
    if len (arr)<=1:
        return arr
    pivot=-1
    left=[]
    right=[]
    n=len(arr)
    for i in range(n-1):
        if arr[i]<arr[pivot]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left)+[arr[pivot]]+quicksort(right)
a=[3,4,5,8,6,7]
print(quicksort(a))