names=("mikey","vijay","siva","prasanna","santhi","chinnu","rockey")
gender=('M','M','M','F','F','F','M')
male=[]
female=[]
for i in range(7):
    if gender[i]=='M':
        male.append(names[i])
    else:
        female.append(names[i])
print(male)
print(female)
c=1
for i in range(len(male)):
    for j in range(len(female)):
        print("TEAM {}:{} and {}".format(c,male[i],female[j]))
        c=c+1