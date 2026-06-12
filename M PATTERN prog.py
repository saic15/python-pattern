a=[[" "for i in range(11)] for i in range(10)]

for i in range(10):
    for j in range(11):
        if j==0 or j==10:
            a[i][j]="*"
        if i==j and i<=5:
            a[i][j]="*"
        if i+j==10 and j>5:
            a[i][j]="*"
          
        
for i in range(10):
    for j in range(11):
        print(a[i][j],end=" ")
    print()

    
    
    
   
