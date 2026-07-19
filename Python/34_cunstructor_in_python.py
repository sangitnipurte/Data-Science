class Employee:

    def __init__(self, salary, name, bond): #This created a instructor
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self): #self is important here because self is a way to referrence the object of the class which being created
        return self.salary
    
    def print_name(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")
e1 = Employee(34000, "Sangit Nipurte", 4)    
print(e1.get_salary())
print(e1.print_name())
e1.print_name