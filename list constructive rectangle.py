class Rect:
    def __init__(self):
        self.l = int(input("Enter length:"))
        self.b = int(input("Enter breadth:"))
    def display(self):
        return self.l*self.b
n=int(input("Enter the num of rectangles:"))
l=[]
for i in range(n):
    R=Rect()
    l.append(R)
for i in l:
    print("Area:",i.display()) 
            
            
      