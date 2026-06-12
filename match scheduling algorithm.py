a=int(input("Enter the num of teams:"))
teams=[]
for i in range(a):
    x=input ("Enter the team name:")
    teams.append(x)
matches=[]
for i in range(a-1):
    for j in range(i+1,a):
        matches.append([teams[i],teams[j]])
pos=1
for i in matches:
    print("MATCHES{}:{}vs{}".format(pos,i[0],i[1]))
    pos=pos+1



    