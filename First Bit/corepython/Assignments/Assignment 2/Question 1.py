#1. Convert the time entered in hh,min and sec into seconds. 

time = int(input("Enter Time in seconds :"))
temp = time

hh = temp // 3600
temp = temp % 3600

min = temp // 60
temp = temp % 60

sec = temp % 60

print(f" hours :{hh}\n minutes :{min}\n seconds :{sec}")