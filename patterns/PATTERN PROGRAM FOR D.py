for row in range(7):
    for col in range(7):
        if(col==2 or col==6)or((row==0 or row==6) and (col!=2 and col!=6)):
            print("*" ,end=" ")
        else:
            print(end="  ")
    print()
