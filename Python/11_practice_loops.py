# # # #Q1
# # # n = int(input("Enter a number: "))
# # # print("The number is:", n)
# # # if n <0:
# # #     print("The number is negative.")
# # # elif n > 0:
# # #     print("The number is positive.")
# # # else :
# # #     print("The number is zero.")

# # #Q2
# # # age = int(input("Enter Your Age:"))
# # # print("Your Age is:", age)

# # # if (age>=18):
# # #     print("You are eligible to vote.")
# # # else:
# # #     print("You are not eligible to vote.")

# # #Q3
# # num = int(input("Enter a number: "))
# # if (num % 2 ==0):
# #     print(num , "Number is Even.")
# # else:
# #     print(num , "Number is Odd.")

# #Q4
# # day = int(input("Enter a number between 1 to 7: "))
# # match day:
# #     case 1:
# #         print("Monday")
# #     case 2:
# #         print("Tuesday")
# #     case 3:
# #         print("Wednesday")
# #     case 4:
# #         print("Thursday")
# #     case 5:
# #         print("Friday")
# #     case 6:
# #         print("Saturday")
# #     case 7:
# #         print("Sunday")

# #Q5 
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# operation = input("Enter the choice: ")

# match operation:
#     case "+":
#         print("Addition :", num1 + num2)
#     case "-":
#         print("Substraction :", num1 - num2)
#     case "*":
#         print("Multiplication :", num1 * num2)
#     case "/":
#         print("Division :", num1 / num2)            


# #Q6
# n = int(input("Enter The Number: "))
# for i in range (1 , 11 ):
    
#     print(n, "X" , i, "=", n*i)  
# 
# Q7  
# sum = 0
# for i in range (1, 101):
   
#     sum+= i
#     print(sum)
    
# #Q8
# for i in range (1, 5):
#     print("*"*i)

#Q9
# sum = 0
# i = 1

# while i<=100:
#     sum +=i
#     i +=1

# print(sum)    

#Q10
# passward = "qwe"
# enter_pass = input("Enter the Password:")
# while enter_pass != passward:
#     enter_pass = input("Wrong pass ! try again: ")
# print ("Success!")    

# #Q11
# num = 4637
# print(int(str(num)[::-1])) #Advanced

for i in range ( 1, 6): 
   match i:
      case 1:
         print(1)
      case 2:
         print(2)
      case 3:
         pass      
      case 4:
         print(4)
      case 5:
         print(5)      