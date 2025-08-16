n = int(input("Entre Number of Emp :"))

total_salary_all = 0


for i in range(1 ,n +1):
    salary = int(input(f"Enter Salary of emp{i}:"))

    if(salary < 20000):
        da = salary * 0.10
        ta = salary * 0.12
        hra = salary * 0.15
        
    else:
        da = salary * 0.15
        ta = salary * 0.18
        hra = salary * 0.20
        
        
        
    total_salary = salary +da +ta+hra
    print(f"Total salary is:{total_salary}")

    total_salary_all += total_salary 
        
print(f"Total salary of All is :{total_salary_all}")