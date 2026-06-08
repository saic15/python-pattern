s=int(input("Enter num of starts:"))
l=int(input("Enter num of lines:"))
b=int(input("Enter num of blocks:"))
for i in range(b):
    c=0
    for j in range(l-i):
        for k in range(s):
            print("*",end=" ")
        print()
    print("-------------------------")
