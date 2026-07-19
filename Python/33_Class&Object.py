#Class is a blue print or a template of a object
#Object is a spacific instance created form a tamplate or class.

class Employee:
    company = "hp"

    def get_salary(self): #self is important here because self is a way to referrence the object of the class which being created
        print(self)
        return 34000
    
e1 = Employee() #An object of an class Employee
print(e1.get_salary()) # Employee e's get salary method is called  

e2 = Employee()
print(e2.get_salary())
print(e2.company)