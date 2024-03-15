n=int(input("enter the numbers of rows :"))
for row in range(n):
    for col in range(n*2):
        if (col==n-row*1 ) or (n+row*1==col and row!=0 ) or (row==round(n/2) and(col>n/2 and (col<round(n/2)+n))):
            print("*",end="")
        else:
            print(end=" ")
    print()
