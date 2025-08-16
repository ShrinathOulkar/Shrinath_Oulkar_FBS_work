#1. Write a program to prompt user to enter userid and password. If Id and  
#password is incorrect give him chance to re-enter the credentials. Let him try 3  
#times. After that program to terminate. 

print('Please enter userid and passward')

id = input("Enter User id :")
passw = int(input("Enter passward :"))

print("User id and Passwaed is created")



for i in range( 1 ,4):
    user = input("enter user id :")
    passward =int(input("Enter Passward :"))
    if(id == user and passw == passward) :
        print("user id and passward is correct")
        break
    else:
        print("user id and passward is incorrect. Try again")
else:
     
    print("program is terminated")