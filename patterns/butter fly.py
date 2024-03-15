for row in range(7):
    for col in range(7):
        if(col==row)or (col==6-row*1 and row!=3) or (row==0 or row==6):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
