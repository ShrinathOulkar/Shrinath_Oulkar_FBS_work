#6. Write a Program to input two angles from user and find third angle of the triangle

ang1 = int(input(" Enter angle 1 : "))
ang2 = int(input(" Enter angle 2 : "))

ang3 = 180- (ang1 + ang2)

print(f"Angle 3rd is : {ang3}")