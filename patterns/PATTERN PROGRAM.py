n=int(input("Enter the number of rows in your pattern: "))
K=1
for i in range(1,n+1):
    for j in range(1,K+1):
        print("@",end=' ')
    K+=2
    print()
