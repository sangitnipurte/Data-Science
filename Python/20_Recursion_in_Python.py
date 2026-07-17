# A function calling itself to solve a problem.
#Fibonacci  Series
n= int(input("Enter a number: "))
def fib(n):
    # Base case of recursion
    if (n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib (n-1)

print(fib(n))

