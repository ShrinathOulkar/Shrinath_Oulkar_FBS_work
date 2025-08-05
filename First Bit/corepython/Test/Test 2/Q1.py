##1. Write a program to accept year from user and check if it is a leap year or not.

year = int(input("Enter Year :"))

if(year % 4 ==0):
    if(year % 100== 0):
        if(year % 400 == 0 ):
            print(" it is a leap year")
        else:
            print("not a leap year")
    else:
        print("It is Leap year")
else:
    print("Not a leap year")

