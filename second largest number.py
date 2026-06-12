a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
c=int(input("Enter a third number:"))
if(a>b and a<c) or (a<b and a>c):
    print("second largest num is:",a)
elif(b>a and b<c) or (b<a or b>c):
    print("second largest num is:",b)
else:
    print("second largest num:")
        