a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
while(b!=0):
    rem=a%b
    temp=b
    b=rem
    a=temp
print(a)
