# b. 1!+ 2! + 3! + 4!+….. + n! 


def factorial_sum(n):
    
    fact = 1
    total = 0
    
    for i in range(1, n+1):
        fact *= i
        total += fact
    print("Sum of factorial series =", total)


n = int(input("Enter n: "))
    
factorial_sum(n)