
# 11. WAP to check if a given number is Armstrong number or not. For 
# each task create separate functions.


def count_digits(num):
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp //= 10
    return count

def sum_of_digits(num, digits):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total

def armstrong(num):
    digits = count_digits(num)                 
    total = sum_of_digits(num, digits)  
    return num == total                        

n = int(input("Enter a number: "))
result = armstrong(n)

if result:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")