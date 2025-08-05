##7. Write a program to check if user has entered correct userid and password. 
print("Create userId and passward")

uid =input("Enter user id :")
passw = int(input("Enter passward :"))

print("userid and passward created")


user = input("enter user id :")
passward =int(input("Enter Passward :"))

if(uid == user):
    if(passw == passward):  
        print("successful login")
    else:
        print("passward is incorrect")
else:
    print("userid is incorrect")