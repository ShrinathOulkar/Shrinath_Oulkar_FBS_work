### 9. Write a program to check if entered number is a palindrome or not. 


def palindrome():
    
    num = int(input("Enter a 3 digit number: "))
    if 100 <= num <= 999:
        first_digit = num // 100
        last_digit = num % 10
        if first_digit == last_digit:
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")
    else:
        print("Please enter a valid 3 digit number.")
        
palindrome()