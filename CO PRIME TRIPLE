def cop(a,b):
    return mikey(a,b)==1
def mikey(a,b):
    while(b!=0):
        rem=a%b
        temp=b 
        b=rem 
        a=temp
    return a 
n=int(input("Enter any num:"))
for a in range(5,n):
    for b in range(4,a):
        for c in range(3,b):
            if c*c+b*b==a*a and cop(a,b) and cop(a,c) and cop(b,c):
                print(c,b,a)
    
