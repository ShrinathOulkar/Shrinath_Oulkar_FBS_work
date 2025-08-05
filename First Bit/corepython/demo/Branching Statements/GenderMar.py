
gender =input("Enter Gender(male/female) :")

age =int(input("Enter age :"))

if((gender == 'M' or 'm') and (age >= 21)) or ((gender == 'F' or 'f')and (age >= 18)):
    
    print("you are eligible for marriage")
    
else :
    print("you are not eligible for marriage")