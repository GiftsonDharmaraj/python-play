n=int(input("enter the nummber of rows : "))
for row in range (n):
    for col in range(n+1):
        if(col==0 ) or (col==n) or (col==row and row<round((n/2)+1) and row!=0) or(col==n-row*1 and row<round(n/2)):
            print("*",end="")
        else:
            print(end=" ")
    print()
