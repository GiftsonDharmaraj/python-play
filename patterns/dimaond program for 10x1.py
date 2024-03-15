n=int(input("Enter the number of rows in your pattern: "))
for i in range(0,round(n/2)):
    for j in range(0,n-i-1):
        print(end="  ")
    for s in range(0,2*i+1):
        print("*",end=" ")
    print()
for i in range(0,round(n)):
    for s in range(0,round(n/2)+i):
        print(end="  ")
    for j in range(0,2*round(n/2)-2*i-1):
        print("* ",end="")
    print()
