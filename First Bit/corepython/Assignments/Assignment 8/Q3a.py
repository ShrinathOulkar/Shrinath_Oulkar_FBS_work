### 3. Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 
# c. 1^1 + 2^2 + 3^3+ …… n^n 

def sum():
    
    sum =0
    n = int(input("Enter value of n :"))
    
    for i in range(1 , n + 1):
        
        sum = sum + i
        
    print(f"Sum of series is {sum}")
    
sum()


