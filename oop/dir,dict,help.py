#dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.
x=[1,2,3,4]
print(dir(x))

#__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("John", 30)
print("\n",p.__dict__)

#help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods
print("\n",help(p))