#break statement
for i in range(1 , 21):
    print(i)
    if i == 11:
        break #cancel the execution of the loop when i is equal to 11

#continue statement
for i in range(1 , 21):
    if i == 11:
        continue #skip the execution of the loop when i is equal to 11
    print(i)

#pass statement
for i in range(1 , 21):
    if i == 11:
        pass #do nothing when i is equal to 11
    print(i)    