import heapq
a=[27,3,4,1,30,23,16,2]
x=[]
for i in a:
    heapq.heappush(x,-i)
s=[]
for i in range(len(a)):
    a=heapq.heappop(x)
    s.append(-a)
print(s)