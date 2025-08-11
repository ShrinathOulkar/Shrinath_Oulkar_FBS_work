### 6. WAP to check if a given number is prime number or not. 


num = int(input("Enter Number :"))

for i in range(2 , num):
#for i in range(2 , num// 2 + 1):

    #print(i)
    
    if(num % i == 0):
        print(f"{num} is not prime number")
        break

else:
    print(f"{num} is prime number")
    
    
    
    
