#1. Write a program to find the area and perimeter of following figure (Accept the 
#length, breadth and radius from user: 

length = float(input("Enter the length : "))
breadth = float(input("Enter the breadth : "))
radius = float(input("Enter the radius : "))

area = (length * breadth) + (0.5 * 3.14 * radius ** 2)

perimeter = (2 * length) + breadth + (3.14 * radius)

print(f"Area of the figure: {area}")
print(f"Perimeter of the figure: {perimeter}")


