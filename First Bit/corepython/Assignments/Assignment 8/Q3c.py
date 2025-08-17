# c. 1^1 + 2^2 + 3^3+ …… n^n 

def sum():
    
    n = int(input("Enter n :"))
    sum = 0
    
    for i in range(1 , n+1):
        
        sum = sum + i**i
    return sum

result = sum()

print(f"Sum of Series is {result}")

