# def sum ( a, b):
#     '''This will sum two numbers'''
#     c = a + b
#     return c

# print(sum.__doc__) #this is used for the write comment into the output or get that information
# print(sum(4, 6))

def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b
print(add.__doc__)
print(add(5, 6))