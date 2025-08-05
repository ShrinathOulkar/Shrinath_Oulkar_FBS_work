#10. Write a program to reverse three-digit number. 

num = int(input("Enter Three digit Number :"))
temp = num

d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

d4 = (d1 * 100) + (d2 * 10) + d3

print(f"Rverse number is:{d4}")