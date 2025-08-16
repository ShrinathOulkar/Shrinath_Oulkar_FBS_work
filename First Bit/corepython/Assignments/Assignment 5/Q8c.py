### c. Find the sum of a geometric series from 1 to n where the common ratio is 2. 

n = int(input("Enter number of terms: "))
sum_geo = 0
term = 1

for i in range(n):
    sum_geo += term
    term *= 2

print(f"Sum of geometric series:", sum_geo)

