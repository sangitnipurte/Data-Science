def sum (a, b):
    print("Hey I my Sangit") 
    c = a + b
    global z #Please Modify global z
    z = 0 #This will refer to global z and create a local variabe 
    return c
z = 3
print(sum(3, 12))
print(z)
