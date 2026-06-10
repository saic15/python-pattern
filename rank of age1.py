names=["SAI","PRASANNA","LAKSHMI","MIKEY","CHANDU"]
age=[30,20,16,38,27]
res=list(zip(age,names))
print(res)
res1=sorted(res,reverse=True)
for i in range(5):
    print("rank {}.{} -{}years old".format(i+1,res1[i][1],res1[i][0]))