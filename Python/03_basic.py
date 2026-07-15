#Variables and Data Types in Python
# In Python, you can create variables to store data. A variable is a name that refers to a value. You can assign a value to a variable using the assignment operator (=). For example:
#Get user input
text = input("Enter some text: ")

#convert the input to uppercase
uppercase_text = text.upper()

#print the uppercase text
print("Uppercase text:", uppercase_text)

#string = name
#integer = age
#float = cgpa
#boolean = is_student
#example

age = 25
cgpa = 9.15
name = "Sangit"

#python is a dynamically typed language.

# 34age = 4 #invalid variable name, because it starts with a number

# a$$ge = 4 #invalid variable name, because it contains special characters

__age = 4 #valid variable name, because it starts with an underscore

#we can only use as a starting (a-z, A-Z, _)
#these are the rule of the python variable  

#integer
age = 25
print(age)
print(type(age))

#float
cgpa = 9.15
print(cgpa)

#string
name = "Sangit"
print(name)

#boolean
is_student = True # can also be False but the T and F are capital 
print(is_student)


