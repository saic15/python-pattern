col="HIT"
class AIML:
    dept="ARTIFICIAL:"
    def set_dim(self,a,b,c,d):
        self.m1=a 
        self.m2=b 
        self.m3=c 
        self.name=d
    def display(self):
        print("1.NAME",self.name)
        print("2.MARKS:",(self.m1+self.m2+self.m3)//3)
        print("3.dept:",AIML.dept)
        print("4.COLLEGE:",col)
class CSE:
    dept="COMPUTER:"
    def set_dim(self,a,b,c,d):
        self.m1=a 
        self.m2=b 
        self.m3=c 
        self.name=d 
    def display(self):
        print("1.NAME",self.name)
        print("2.MARKS:",(self.m1+self.m2+self.m3)//3)
        print("3.dept:",CSE.dept)
        print("4.COLLEGE:",col)

S1=AIML()
S2=AIML()
C1=CSE()
C2=CSE()
S1.set_dim(20,30,40,"sai")
S2.set_dim( 50,60,70,"prasanna")
S1.display()
S2.display()
C1.set_dim( 25,35,45,"mikey")
C2.set_dim(55,65,75,"siva")
C1.display()
C2.display()


    