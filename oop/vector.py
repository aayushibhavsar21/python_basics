class vector:
    def __init__(self,x,y,z):
        self.i=x
        self.j=y
        self.k=z

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return vector(self.i+x.i,self.j+x.j,self.k+x.k)

v1=vector(2,3,4)
print(v1)
v2=vector(5,6,4)
print(v2)
print(v1+v2)