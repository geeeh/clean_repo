class Circle():
    def __init__(self, radius):
        self.radius=radius
        self.diameter=self.radius*2

    def area(self):
        return(3.142*self.radius**2)

    def circumference(self):
        return(3.142*self.diameter)

class my_circle(Circle):
    def __init__(self, radius, color):
        Circle.__init__(self, radius)
        self.color=color
        

cir= my_circle(7,"blue")
print(cir.color)
print(cir.area())

        
        




