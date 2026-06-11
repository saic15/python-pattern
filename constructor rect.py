class Rect:
    def __init__(self,a,b):
        self.l = a
        self.b = b 
        self.display()
    def display(self):
        print("Area:",self.l*self.b)
r=Rect(10,20)
s=Rect(13,14)
        