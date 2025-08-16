### a. 1! + 2! + 3! + 4! + …..n!

num = int(input("Enter a number: "))
fact_sum = 0
for i in range(1,num +  1):
    fact = 1
    for j in range(1,i +1):
        fact = fact * j
    fact_sum += fact
    
print(f"sum of factorial is {fact_sum}")



    