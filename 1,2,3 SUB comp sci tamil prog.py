comp=["raju","pavi","anu","meera","mamitha"]
sci=["raju","pavi","rose","pinkey","amala"]
tamil=["raju","ram","rose","meera","vickey"]
comp1=set(comp)
sci1=set(sci)
tamil1=set(tamil)
a=comp1&sci1
b=comp1&tamil1
c=tamil1&sci1
res=a|b|c
three = comp1 & sci1 & tamil1
two=res-three
u=comp1|sci1|tamil1
x=two|three 
result=u-x
print(three)
print(two)
print(result)
