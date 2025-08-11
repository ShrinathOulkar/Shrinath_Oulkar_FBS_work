### 3. WAP to print sum of series upto n. 

n = int(input("Enter Number :"))

i = 1
sum_series = 0

while(i <= n):
    sum_series = sum_series + i
    i = i + 1
    
print(f"Sum of series is :{sum_series}")