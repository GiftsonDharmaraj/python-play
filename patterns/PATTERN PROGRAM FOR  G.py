for  row in range (10):
    for col in range(5):
        if((col==0) and (row!=0 and row<8))or (row==0) or (row==4 and col>2 and col<4)  or (col==2 and row>3 and row<8) or (row==7 and col>0 and col<2) or (col==4 and row>3 and row<8) :
            print("* ",end="")
        else:
            print(end="  ")
    print()
