#       1   
#     1   1   
#   1   2   1
# 1   3   3   1


for i in range (1 , 5):
    
    for j in range(1 ,5 - i):
        print(" " , end= " ")
    c = 1
    for j in range(1 ,i + 1  ):
        print(c , end ="   ")
        
        c = int(c*(i-j)/j)
        
    print()
    
print()
    
for i in range (0 , 4):
    
    for j in range(0 ,4 - i):
        print(" " , end= " ")
    c = 1
    for j in range(0 ,i + 1  ):
        print(c , end ="   ")
        
        c = int(c*(i-j)/(j + 1))
        
    print()

