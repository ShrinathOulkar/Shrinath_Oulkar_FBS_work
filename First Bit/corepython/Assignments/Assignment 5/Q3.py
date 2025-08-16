#3. Accept no. of passengers from user and per ticket cost. Then accept age of each  
#passenger and then calculate total amount to ticket to travel for all of them based on  
#following condition : 
#a. Children below 12 = 30% discount 
#b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full.


num = int(input("Enter Number of Passangers :"))
cost=int(input("Enter cost of Ticket :"))
total_amt = 0

for i in range(1 , num+1):
    age =int(input("Enter Age of passanger :"))
    
    if (age < 12):
        dis_amt = cost * 0.3
        total_amt += cost - dis_amt
    elif (age > 59):
        dis_amt = cost * 0.5
        total_amt += cost - dis_amt
    else:
        total_amt += cost
    
    
print(f"Total amount to be paid :{total_amt}")

