###5. Write a program to check whether the triangle is equilateral, isosceles or scalene  triangle. 

a = int(input("Enter 1st angle :"))
b = int(input("Enter 2nd angle :"))
c = int(input("Enter 3rd angle :"))

if(a == b and b == c ):
    print("Triangle is Equlateral")
elif(a == b or b == c or c == a):
    print("Triangle is Isoscales")
else:
    print("Triangle is Scalene")

