n=int(input("enter the number of rows: "))
for i in range(0,round(n/2)):
    for s in range(0,n-i-1):
        print(end="  ")
    for j in range(0,2*i+1):
        print("* ",end="")
    print()
for i in range(0,n):
    for s in range(0,i*):
        print(end="  ")
    for j in range(0,(2*round(n/2)-2*i-1)):
        print("* ",end="")
    print()
