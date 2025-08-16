

for i in range( 1 , 6):
    
    for j in range( 1 , 6 - i):
        print(" ", end = " ")
        
    for j in range( 1 , 6):
        if( j == 1):
            print("1", end = "   ")
        elif(i == 5 or i == j):
            print(j , end = "   ")
        else:
            print(" ", end = "   ")
            
        
    print()