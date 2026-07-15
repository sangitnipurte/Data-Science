# #if_else_statemet
# age = int(input("Enter the Age::  "))

# if (age>18):
#     print("You are eligible to vote") #condition
# else:
#     print("You are not eligible to vote") #condition

# print("This is the end of the program") # this statement is not part of the if else statement, it will be executed in any case


#if_elif_else_statement
age = int(input("Age:"))

if (age>18):
    print("You can drive")
elif(age<18):
    print("you cant drive")
elif(age==18):
    print("you are eligible to drive")
else:
    print("you are small")        