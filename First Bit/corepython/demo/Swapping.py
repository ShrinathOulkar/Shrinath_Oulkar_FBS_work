### Swapping Numbers

x = int(input("Enter X : "))

y = int(input("Enter Y : "))

print(f"Before swap : {x} ,{y}")

# using third Variable

#z = x
#x = y
#y = z 

## without using third variable
x = x + y
y = x - y
x = x - y

## with using python

# x ,y =y ,x

print(f"After swap : {x} ,{y}")
