# # # # # # #Q1
# # # # # # def greek():
# # # # # #     print("Hello, Python Learner!")
# # # # # # greek()

# # # # # #Q2
# # # # # def sqr(n):
# # # # #     c = n*n
# # # # #     return c
# # # # # print(sqr(1))
# # # # # print(sqr(2))
# # # # # print(sqr(3))
# # # # # print(sqr(4))
# # # # # print(sqr(5))

# # # # #Q3
# # # # def name(first, last):
# # # #     return f"{first} {last}"
# # # # print(name("Sangit","Nipurte"))

# # # #Q4
# # # def area(lenght, width = 10):
# # #     s = lenght * width
# # #     return s
# # # print(area(5, 12 ))

# # #Q5

# # # add = lambda a, b: a+b
# # # print(add(4, 6))

# # #Q6
# # # square = lambda x : x*x
# # # list1 = [1,2,3,4,5]
# # # print(list(map( square, list1 )))

# # #Q7
# # def fact(n):
# #     if n == 0 or n==1:
# #         return 1
# #     return fact(n - 1)*n
# # print(fact(4))

# #Q8
# def sum_of_digit(n):
#     if n == 0 :
#         return 0
#     return n%10 + sum_of_digit(n//10)

# print(sum_of_digit(42343425))

#Q9
# import math

# a = math.sqrt(144)
# b = math.sin( math.radians(90))

# print (a, b)

# #Q10
# import requests
# a = requests.get("https://api.github.com/")
# print(a.json())

#Q11
# def increment():
#     counter = 0
#     counter +=1
#     print(counter)
# increment()
# increment()

#Q12
# def mul(a, b):
#     '''multiply function '''
#     return a * b
# print(mul(5 , 7))
# print(mul.__doc__)
# help(mul)

#Q13
# def fib(n):
#     if (n == 0 or n == 1):
#         return n
#     return fib(n-2) +fib(n-1)
# print(fib(4))

#Q14
def safe_divide(a, b):
    if (b == 0):
        return ("Cannot divide by zero")
    return a/ b
print(safe_divide(4,0))

#solve this problem letter
#Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.