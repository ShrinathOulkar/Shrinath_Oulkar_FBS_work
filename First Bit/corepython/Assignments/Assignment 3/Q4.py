##4. Write a program to input all sides of a triangle and check whether triangle is valid or not

a = int(input("Enter 1st side :"))
b = int(input("Enter 2nd side :"))
c = int(input("Enter 3rd side :"))

if(a + b> c)and(a + c > b ) and (c + b > a):
    
    print("Triangle is valid")
else:
    print("Triangle is Invalid")