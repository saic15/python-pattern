a=10
b=12
big=max(a,b)
step=big
while(True):
    if big%a==0 and big%b==0:
        break
    else:
        big=big+step
print(big)
