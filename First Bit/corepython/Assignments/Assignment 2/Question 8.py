#8. Write a program to swap two numbers using third variable. 


x = int(input("Enter X : "))

y = int(input("Enter Y : "))

print(f"Before swap : {x} ,{y}")

# using third Variable

z = x
x = y
y = z 

print(f"After swap : {x} ,{y}")
