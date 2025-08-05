#5. WAP to calculate selling price of book based on cost price and discount. 

cp = int(input("Enter cost price :"))

dis = int(input("Enter Discount :"))



disp = cp * (dis / 100)
sp = disp + cp

print(f"Selling price is : {sp}")