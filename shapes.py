def sq():
    a=int(input("Enter any side:"))
    print(a*a)
def rect(a,b):
    print(a*b)
def tri():
    b=int(input("Enter any base:"))
    h=int(input("Enter ht: "))
    return 0.5*b*h
def cir(r):
    return 3.14*r*r 
print("1.SQUARE")
print("2.RECTANGLE")
print("3.TRIANGLE")
print("4.circle")
ch=int(input ("Enter any choice:"))
if ch==1:
    sq()
elif ch==2:
    a=int(input("Enter the length of the rectangle:"))
    b=int(input("Enter the breadth of the rectangle:"))
    rect(a,b)
elif ch==3:
    x=tri()
    print(x)
else:
    r=int(input("Enter the radius:"))
    x=cir(r)
    print(x)
            
            
        