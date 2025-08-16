### a. 1/1! + 2/2! + 3/3! + …..n/n!


num = int(input("Enter a number: "))
sum_of_series= 0
for i in range(1,num +  1):
    fact = 1
    for j in range(1,i +1):
        fact = fact * j
    sum_of_series += i /fact
    
print(f"sum of series is :{sum_of_series}")



    