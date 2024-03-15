n=int(input("enter the number of rows you want: "))
for row in range(n):
    for col in range(n-2):
        if(col==0)or( row==0 and (col>0 and col<n/2)) or (col==round(n/2)and row>0 and  row<=n/2-1) or row==round(n/2) and col>0 and col<=n/2-1:
            print("*",end="")        
        else:
            print(end=" ")
    print()
            
