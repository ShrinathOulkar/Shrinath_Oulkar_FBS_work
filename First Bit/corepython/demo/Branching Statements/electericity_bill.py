units = int(input("Enter Electricity Units: "))

if units >= 0:
    if units <= 50:
        bill = units * 0.5
    elif units <= 150:
        bill = (50 * 0.5) + (units - 50) * 0.75
    elif units <= 250:
        bill = (50 * 0.5) + (100 * 0.75) + (units - 150) * 1.20
    else:
        bill = (50 * 0.5) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50

    subcharge = bill * 0.20
    total_bill = bill + subcharge

    print(f"Total Bill is: ₹{total_bill:.2f}")
else:
    print("Invalid input. Units cannot be negative.")
