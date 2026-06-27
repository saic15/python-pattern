class Graph:
    def __init__(self,v):
        self.adj=[[]for i in range(v)]
    def add_edge(self,a,b):
        self.adj[a].append(b)
        self.adj[b].append(a)
    def dispay(self):
        for i in range(len(self.adj)):
            print("vertex{}:".format(i),end=" ")
            for j in self.adj[i]:
                print(j,end="-->")
            print()
x=Graph(6)
x.add_edge(0,1)
x.add_edge(0,2)
x.add_edge(1,2)
x.add_edge(1,4)
x.add_edge(2,5)
x.add_edge(2,4)
x.add_edge(2,3)
x.add_edge(3,5)
x.dispay()
             
            
            
             
                