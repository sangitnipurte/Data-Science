#   #1. Create a list fruits = ["apple", "banana", "cherry"].

#  Print the first fruit.
#  Replace "banana" with "orange".
#  Print the length of the list.
#  Solution
#    list1 = ["apple", "banana", "cherry"]
#    print(list1[0])
#  list1[1]= "Orange"
#    print(len(list1))
#    print(list1)

#  Q2. Create a list of numbers from 1 to 10.
# Print the first three numbers using slicing.
#   Print the last three numbers using slicing.

#  list1 = [i for i in range(1,11  )]
#  print(list1)

#  print(list1[0: 3])
#  print(list1[-3: 
#Q3. Start with numbers = [5, 2, 9, 1, 7] and do the following

#  Sort the list in ascending order.
#  Append the number 10 to the list.
#  Remove the number 2 from the list.

# list1 = [5, 2, 9, 1, 7]
# print(list1)

# list1.sort()
# print(list1)

# list1.append(10)
# print(list1)

# list1.remove(2)
# print(list1)

# Q4. Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.

# list1 =["Alice", "Bob", "Charlie"]
# list1.insert(1, "David")
# print(list1)

# Q5. Create a tuple coordinates = (10, 20) and print both elements.

# coordinates = (10, 20)
# print(coordinates)

# coordinates = (10, 20)
# print(coordinates[0])
# print(coordinates[1])

#Q6 Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
#This is not possible in the Tuble because the tuples are not changable

#Q7 Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

# coordinates = (10, 20)
# list1 = list(coordinates)
# print(list1)
# list1[0] = 50
# coordinates = tuple(list1)
# print(coordinates)

#Q8. Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
# my_set = {1, 2, 3, 3, 4} 
# print(my_set) # The 3 is printed at one time only

#Add 5 to the set, remove 2, and check if 4 is in the set.

# my_set.add(5)
# print(my_set)
# my_set.remove(2)
# print(my_set)
# # print(my_set[4])

#Q9. Create two sets:
# a = {1, 2, 3}

# b = {3, 4, 5}
# Find their:
# Union
# print(a.union(b))

# Intersection
# print(a.intersection(b))
# Difference (a - b)
# print(a.difference(b))

#Q10Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
# student = {"name": "John", "age": 20, "grade": "A"}
# print(student)
# Print the value of "name".
# print(student["name"])

# Change "grade" to "A+".
# student["grade"] = "A+"
# print(student)

# Add a new key "city" with value "Delhi".
# student["city"] = "Delhi"
# print(student)

#Q11 Create a dictionary of three friends and their phone numbers. Use:
# friends = {"Sangit": 7854989032, "Tanmay": 98375209258, "Yash" : 983270258}

# keys() to get all names
# print(friends.keys())

# values() to get all numbers
# print(friends.values())

# items() to loop over key-value pairs and print them
# print(friends.items())

#Bonus Qs
# Q1 Write a program that takes a list of numbers and removes all duplicates using a set.
# Q2 Given a dictionary of products and their prices, find the product with the highest price.
# Q3 Write a program that merges two dictionaries into one.