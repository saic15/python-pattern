head=int(input("Enter total number of heads:"))
legs=int(input("Enter total number of legs:"))
flag=False
for cow in range(0,head+1):
    hens=head-cow
    total_legs=(cow*4)+(hens*2)
    if total_legs==legs:
        print("Cows:",cow)
        print("Hens:",hens)
        flag=True
        break
if not flag:
    print("no solution")
   