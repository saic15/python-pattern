n=20
x=[]
while(True):
    if n in x and n!=1:
        print("not round")
        break
    if n==1:
        print("round")
        break
    x.append(n)
    n=sum([int(i)*int(i) for i in str(n)])
print(x)