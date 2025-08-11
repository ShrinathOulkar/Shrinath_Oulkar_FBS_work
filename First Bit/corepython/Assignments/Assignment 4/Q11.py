### 11. WAP to check if given number Strong Number. 

num = int(input("Enter number :"))

sum =0
temp = num

while(temp > 0):
    
    d1 = temp % 10
    temp = temp // 10
    
    i = 1
    fact = 1
    while(i <= d1):
        fact = fact * i
        i = i + 1 
        
    sum = sum + fact

if(sum == num):
    print(f"{num} is strong number ")
else:
    print(f"{num} is not strong number ")

        
