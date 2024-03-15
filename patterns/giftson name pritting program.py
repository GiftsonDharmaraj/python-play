print_g =[[" " for i in range(7)] for j in range(7)]
print_I =[[" " for i in range(7)] for j in range(5)]
print_f =[[" " for i in range(7)] for j in range(5)]
#print_t =[[" " for i in range()] for j in range()]
#print_s =[[" " for i in range()] for j in range()]
#print_o =[[" " for i in range()] for j in range()]
#print_n =[[" " for i in range()] for j in range()]
#code for G
for row in range(0,7):    
    for col in range(0,7):     
        if ((col == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and col > 1 and col < 5) or (row == 3 and col > 2 and col < 6) or (col == 5 and row != 0 and row != 2 and row != 6)):
            print_g[row][col]="*"
#code for I
for row in range(0,7):
    for col in range(0,5):
        if(col==2 and( row!=0 and row!=6)) or (row==0 or row==6):
            print_I[row][col]="*"

#code for F
for row in range(7):
    for col in range(5):
        if(col==0)or((row==0 or row==3 ) and col>0):
            print_f[row][col]="*"
for i in range (0,7):
   for j in range(0,7):
       print(print_g[i][j],end=" ")
   print(end=" ")
   for j in range(0,5):
        print(print_I[i][j],end=" ")
   print(end=" ")
   for j in range(0,5):
       print(print_f[i][j],end=" ")
   print(end=" ")
   print()
