n=int(input("enter the number of rows you want : "))
for row in range(0,n):
    for col in range(0,n-2):
     if ((col==0 or col==n-3) ) or ((row==0 or row==n/2) and(col>0 and col<n-3)):
            print("* ",end=" ")
     else:
            print(end=" ")
