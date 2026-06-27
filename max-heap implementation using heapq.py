import heapq
a=[27,3,4,1,30,23,16,2]
x=[]
for i in a:
    heapq.heappush(x,-i)
heapq.heappop(x)
print(x)
x1=[-i for i in x]
print(x1)