### 4. Sum of all odd numbers between 1 to n  

def sum_odd():
    
    n = int(input("Enter n :"))
    
    sum = 0
    for i in range(1 , n + 1):
        if(i % 2 != 0):
            
            sum = sum + i
            
    print(f"Sum of odd numbers is {sum}")
    
    
