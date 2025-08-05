#13. Write a program to input electricity unit charges and calculate total electricity bill 
#according to the given condition: 
#For first 50 units Rs. 0.50/unit 
#For next 100 units Rs. 0.75/unit 
#For next 100 units Rs. 1.20/unit 
#For unit above 250 Rs. 1.50/unit 
#An additional surcharge of 20% is added to the bill

units = int(input("Eneter Electeric unit :"))

bill =0

if(units > 0):
    if(units > 50):
        if(units > 150):
            if(units <= 250):
                if(units > 250):
                    bill = (50 * 0.5) + (100 * 0.75) + (100 * 1.20) + (units - 250)*1.50
                else:
                    bill = (50 * 0.5) + (100 * 0.75) + ( units -150)* 1.20
            else:
                bill = (50 * 0.5) + (100 * 0.75) + (units * 1.20)
        else:
            bill = (50 * 0.5) + (units - 50 )* 0.75
    else:
        bill = units * 0.5
else:
    print("invalid input :")
    
subcharge = bill * (20/100)

total_bill = bill + subcharge

print(f"Total Bill is : {total_bill}")