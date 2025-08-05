#2.Write a program to accept 3 digit number. If first digit is double of second digit and half of
#third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
#Eg : - 428 , 214 etc.

num = int(input("Enter 3 digit number :"))



num1  = num // 100

num2 = (num //10)%10

num3 = num % 10

if(num1 == 2*num2 and num1== num3/2):
    print("Yes, you have done it")
else:
    print("Please try next time")