up=0
lw=0
a="r"
while(a not in "aAeEiIoOuU"):
    a=input("enter any char:")
    if a in "aAeEiIoOuU":
        break
    if a.isupper():
         up=up+1
else:
    lw=lw+1
print("upper case:",up)
print("lower case:",lw)