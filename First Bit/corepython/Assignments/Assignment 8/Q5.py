def Prime_Sum():
    total = 0
    n = int(input("Enter n :"))
    
    for num in range(2, n+1):
        prime = True   
        for i in range(2, num // 2 + 1): 
            if num % i == 0:
                prime = False
                break   
        if prime:
            total = total + num
    
    print(f"Sum of prime numbers is {total}")

Prime_Sum()
