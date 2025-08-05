#8. Write a program to prompt user to enter userid and password. After verifying 
#userid and password display a 4 digit random number and ask user to enter the 
#same. If user enters the same number then show him success message otherwise 
#failed. (Something like captcha) 

import random

uid =input("Enter user id :")
passw = int(input("Enter passward :"))

a = input("Enter The User ID:")
b = input("Enter The Password:")

if (uid == a) and (passw == b):
    print("Login Successful")

    captcha = random.randint(1000,9999)
    print(f'Catcha Number:{captcha}')

    user_captcha = int(input("Enter the Catcha:"))

    if (captcha == user_captcha):
        print("Success")
    else:
        print("Faild")

else:
    print("Invaild User ID or Password")