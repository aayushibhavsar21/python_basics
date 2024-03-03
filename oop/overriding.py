class rect:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y

class square(rect):
    def __init__(self,x):
        self.len=x
        super().__init__(self.len,self.len)

    def area(self):
        return super().area()

class circle(rect):
    def __init__(self, x):
        self.radius=x
        super().__init__(self.radius,self.radius)

    def area(self):
        return 3.14*super().area()

a=rect(3,5)
print(a.area())
b=square(3)
print(b.area())
c=circle(5)
print(c.area())
