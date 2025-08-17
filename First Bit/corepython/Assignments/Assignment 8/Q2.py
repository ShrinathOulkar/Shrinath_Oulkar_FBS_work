### 2. Write a program to calculate area of circle 

def area_circle( r ):
    
    
    Area = 3.14 * r * r
    
    return Area

r = int(input("Enter Radius :"))
result = area_circle(r)

print(f"Area of Circle is { result }")

