names=("SAI","PRSANNA","LAKSHMI","MIKEY","CHANDU")
marks=(90,80,25,99,36)
pos=1
for i in range(5):
    if marks[i]>40:
         print("{}.{} has scored{}%".format(pos,names[i],marks[i]))
         pos=pos+1
   
