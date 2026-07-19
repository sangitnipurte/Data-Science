class vector:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def sum (self, p):
        return vector((self.x +p.x) , (self.y + p.y))
    
    def print_point(self):
        print (f"x is {self.x} and y is {self.y}")

    #this is called method overriding    
    def __add__(self, p):
        return vector((self.x +p.x) , (self.y + p.y))

p1 = vector(3, 4)
p2 = vector(5, 6)        

# p = p1.sum(p2)
p = p1 + p2
p.print_point()