##6. Write a program to calculate profit or loss. 

cp = int(input("Enter Cost Price :"))
sp = int(input("Enter Selling Price :"))

if(sp > cp):
    print("You are in Profit")
elif(cp > sp):
    print("You are in Loss ")
else:
    print("You have not profit and Loss")
