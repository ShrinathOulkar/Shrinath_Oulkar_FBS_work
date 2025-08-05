#4. Write a program to enter P, T, R and calculate simple Interest
p = int(input("Enter principal : "))
r = float(input("Enter rate : "))
t = int(input("Enter Time : "))

si = (p * r * t)/100

print(f"Simple Interest is :{ si } ")