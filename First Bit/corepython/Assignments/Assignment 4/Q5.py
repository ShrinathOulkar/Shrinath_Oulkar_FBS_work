### 5. WAP to print Fibonacci series upto n.

n = int(input("Enter Number :"))
a = 0 
b = 1
count = 0
print(a , b , end=" ")
while(count < n):
    c = a + b
    print(c,end =" ")
    a ,b = b ,c
    count = count + 1    


