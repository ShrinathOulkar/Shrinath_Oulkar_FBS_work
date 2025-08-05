#6. WAP to calculate total salary of employee based on basic, da=10% of basic, 
#ta=12% of basic, hra=15% of basic.

sal = int(input("Enter salary : "))

da = sal * 0.1 # basic * 10/100
ta = sal *0.12
hra = sal * 0.15

total_salary = sal + da +ta +hra

print(f"Total Salary Amount :{total_salary}")