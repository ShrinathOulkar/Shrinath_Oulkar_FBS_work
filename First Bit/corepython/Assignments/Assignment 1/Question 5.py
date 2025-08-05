#5. Write a program to enter P, T, R and calculate Compound Interest. 

p = int(input("Enter principal : "))
r = float(input("Enter rate : "))
t = int(input("Enter Time : "))

ci = p * (1 + (r/100))**t - p

print(f"Compound Interest is :{ ci } ")