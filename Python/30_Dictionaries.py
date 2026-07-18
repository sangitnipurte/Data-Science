# # marks = {"Sangit": 25, "Jack": 34, "Tanmay": 74}
# # # print(marks, type(marks)) #Using the type keyword find the type of any datatype

# # #How we can access dictionary
# # print(marks["Tanmay"])
# # marks["Sangit"] = 98 #you can change the values of the dictionary
# # print(marks)

# #Common Dictionary Methods
# marks = {"Sangit": 25, "Jack": 34, "Tanmay": 74}
# print(marks.keys()) #key are the left side entities
# print(marks.values()) #values are the  right side entities

# print(marks.clear()) #Used for clear the dictionary
# marks.pop("Sangit")
# print(marks)

#Dictionary Comprehension

table_of_5 = {i: 5*i for i in range(1, 11)}
print(table_of_5)