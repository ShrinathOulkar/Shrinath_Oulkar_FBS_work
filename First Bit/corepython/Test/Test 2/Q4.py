#4. Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

height = int(input("Enter the height of wall :"))
width = int(input("Enter the width of wall :"))
cost = int(input("Enter cost of painting(sq.m) :"))

walls = (height * width)* 4

cost_paint = walls * cost

print(f"Cost of painting of All walls is :{cost_paint}")