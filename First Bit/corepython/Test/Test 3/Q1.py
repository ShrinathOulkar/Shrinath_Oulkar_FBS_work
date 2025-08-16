### write program to print first n prime numbers

n = int(input("Enter number :"))
num = 2
count = 0
while(count < n):
    
    for i in range(2, num//2 + 1):
    
        if(num %  i== 0):
            break
    else:
        print(num)
        count += 1
    num += 1

