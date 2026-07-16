# def add(a, b): # a and b are the variable names or parameters
#     x = a + b
#     return x
# c = add(2, 3) # 2 and 3 called arguments
# d = add( 34, 7)
# print(d)
# print(c)

#Types of Arguments
#1 : Positional Argument

# def add(a, b): # a and b are the variable names or parameters
#     x = a + b
#     return x
# c = add(2, 3) # 2 and 3 called arguments
# d = add( 34, 7)
# print(d)
# print(c)

#2 : Default Argument
# def add (x, z, y=0): # The value of Y is set default ie y = 0
#     return x+ y+ z
# print(add(3, 6 ))

#3 : Keyword Argument
def add(a, b):
    return a+ b
print(add ( b = 12, a= 3)) #this value is return by user that called the keyword argument in any ordered like this( b = 12, a= 3)