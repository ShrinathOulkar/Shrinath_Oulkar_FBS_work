##3. Write a program to input angles of a triangle and check whether triangle is valid or not. 

a = int(input("Enter 1st angle :"))
b = int(input("Enter 2nd angle :"))
c = int(input("Enter 3rd angle :"))

tri = a + b + c

if( tri == 180):
    print("Triangle is Valid")
else:
    print("Triangle is invalid")