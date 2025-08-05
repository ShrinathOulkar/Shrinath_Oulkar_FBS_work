### 3. Convert distance given in feet and inches into meter and centimeter. 

feet = int(input("Enter distance in Feet :"))

inch = int(input("Enter distance in Inches :"))

d = ((feet * 30.48) + (inch * 2.54)) / 100

e  = d * 100

print(f'{d} meters')

print(f'{e} centimeter')