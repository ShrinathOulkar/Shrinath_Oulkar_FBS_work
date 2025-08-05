#7. Program to Find the Roots of a Quadratic Equation

a =int(input("Enter a value : "))
b =int(input("Enter b value : "))
c =int(input("Enter c value : "))

sqrt = ((b**2) - (4*a*c))**0.5

res1 = (-b + sqrt)/2*a
res2 = (-b - sqrt)/2*a

print(f"Result 1 is : {res1}")
print(f"Result 2 is : {res2}")
 