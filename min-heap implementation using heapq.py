import heapq
a=[27,3,4,1,30,23,16,2]
x=[]
for i in a:
    heapq.heappush(x,i)
print(x)
heapq.heappop(x)
print(x)