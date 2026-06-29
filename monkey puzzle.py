def monkey(x,y,z):
    ht=0
    time=0
    i=1
    while(True):
        if ht==x or ht>x:
            break
        if i%2==1:
            ht=ht+y  
            time=time+1
        else:
            ht=ht-z
            time=time+1
        i=i+1
    print(time)
monkey(30,10,5)
monkey(21,5,3)