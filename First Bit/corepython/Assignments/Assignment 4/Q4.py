### 4. WAP to print factorial of a number . 

n = int(input("Enter Number :"))

i = 1
fact = 1

while(i <= n):
    fact = fact * i
    print(i)
    i= i + 1
    
print(f"Factorial is :{fact}")
