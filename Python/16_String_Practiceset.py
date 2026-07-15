#Q1
# name = "Sangit Vilas Nipurte"
# print(name[0])
# print(name[-1])
# print(len(name))

#Q2
# str1 = "Hello"
# str2 = "World"
# print(str1+" "+str2)

#Q3
# text = "Python Programming"
# print(text[:6])
# print(text[-6:])
# print(text[0:20:2])

#Q4
# text = "Python Programming"
# print(text[::-1])

#Q5
# text = "  i love python programming  "
# print(text.strip())
# print(text.title())
# print(text.count("o"))

#Q6
# text = "123abc"
# print(text.isalnum())

#Q7
# name = "JOHN" 
# age = 25
# print(f"My {name} is John and I am {25} years old.")
# print("My {} is John and I am {} years old.".format(name, age))

#Q8
# text = "Coding in Python is fun"
# print(text.replace("fun", "awsome"))
# print(text.find("Python"))
# print(text.upper())

#Q9
# text = "Coding in Python is fun"
# sum = 0
# vowels = {'a','e','i','o','u'}

#Q10
# for char in text:
#     if(char in vowels):
#         sum += 1
# print(f"There are {sum} vowels in this text")        

#Q11
str1= "madams"

if (str1 == str1[::-1]):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")
