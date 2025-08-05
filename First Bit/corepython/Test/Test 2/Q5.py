#5. A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST

p1 = int(input("Enter the price of poduct 1 :"))
p2 = int(input("Enter the price of poduct 2 :"))
p3 = int(input("Enter the price of poduct 3 :"))
p4 = int(input("Enter the price of poduct 4 :"))
p5 = int(input("Enter the price of poduct 5 :"))

all_price = (p1 + p2 + p3 + p4 + p5)
gst = all_price * 0.18

total_price = all_price + gst




print(f"Total Bill is :{total_price}")

