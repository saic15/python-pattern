import heapq
a=(3,2,1,5,6,4)
k=2
x=[]
for i in a:
    heapq.heappush(x,-i)
for i in range(k):
    res=heapq.heappop(x)
print(res)