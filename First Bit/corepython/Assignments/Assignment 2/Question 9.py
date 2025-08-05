#9. Write a program to swap two numbers without using third variable. 

x = int(input("Enter X : "))

y = int(input("Enter Y : "))

print(f"Before swap : {x} ,{y}")

## without using third variable
x = x + y
y = x - y
x = x - y

print(f"After swap : {x} ,{y}")
