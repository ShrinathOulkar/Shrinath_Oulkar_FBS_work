### 6. Write a program to find print the following Fibonacci series using functions: 
#    1  1  2  3 5 8  n terms 

def fibonacci():
    
    num = int(input("Enter n :"))
    a = 1
    b = 0

    for i in range(num):## range(1 , num + 1)
        c = a + b
        print(c ,end=" ")
        a = b
        b = c
    
fibonacci()

