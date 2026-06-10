names=["sai","mikey","prasanna","bob","siva"]
marks=[[23,33,43],[55,66,77],[30,40,50],[88,99,77],[35,45,55]]
for i in range(5):
    avg=sum(marks[i])//3
print("{}.{} has scored{}%".format(i+1,names[i],avg))