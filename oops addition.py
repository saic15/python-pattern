class abc:
    dept="cse"
    def set_dim(self):
        x=int(input("Enter num1:"))
        y=int(input("Enter num2:"))
        self.a=x 
        self.b=y
    def display(self):
        print(self.a+self.b)
        print(abc.dept)
a1=abc()
a2=abc()
a1.set_dim()
a1.display()
a2.set_dim()
a2.display()

           