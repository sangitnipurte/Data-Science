# name =  "Sangit" #Strings are immutable

# # Name[0] = "R" #we can't do this. That gives a runtime error
# a = len(name) # len gives a length of the string
# print(a)

# nam = "Hello world"
# s = len(nam) # len gives a length of the string
# print(s)
# #syntax
# #print(text._____())
# print(nam.upper())# use for all upper case
# print(nam.lower())#use for all in lower case
# print(nam.capitalize()) # capital letter first

# text = "  hello world  "
# print(text.strip())  # Output: "hello world"
# print(text.lstrip()) # Output: "hello world  "
# print(text.rstrip()) # Output: "  hello world"

# text = "Python is fun ans fun and fun"
# print(text.find("is"))   # Output: 7
# print(text.replace("fun", "awesome"))  # Output: "Python is awesome"

# text = "Apple,Banana,Mango"
# print(text.split((","))) #use to seperate out
# print((",".join(['Apple', 'Banana', 'Mango']))) #used to join a list
# #list of collection of data

#Cheching Strings Properties
text = "Python123"
print(text.isalpha())  # Output: False all characters are alphabet or not
print(text.isdigit())  # Output: False all characters are digit or nor
print(text.isalnum())  # Output: True alnum means a sttring which is content alphabet and numbers
print(text.isspace())  # Output: False 