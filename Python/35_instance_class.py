class Employee:

    company = "MSI" #This is class attribute

    def __init__(self, salary, name, bond, company): 
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    def get_salary(self): 
        return self.salary
    
    def print_name(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

e1 = Employee(23900, "Durvesh", 3, "Tesla" )
print(e1.company)  #will always print instance attribute whenever present here is a  self.company = company is a print attribute otherwise the class attribute is present

#Object introspection
print(dir(e1)) #thats print all methods and attribute of the e1 

print(Employee.company) #thats print the class attribute ie Employee is a name of class