class student:
    school="xyz"                    #class variable which is same for all instance(object)
    def __init__(self,name,marks):
        self.name = name             #instance variable which is different for all instance(object)
        self.marks = marks           #instance variable which is different for all instance(object)
    def info(self):
        print(f"{self.name} from {self.school} has {self.marks[0]} in sub1 , {self.marks[1]} in sub2 and {self.marks[2]} in sub3 ")

    @staticmethod
    def add(a,b):
        print()
        print(a+b)

a=student("aayushi",[23,67,98])
a.info()
b=student("krutika",[37,27,83])
b.school="abc"  #instance variable #at execution class variable is only get print if instance variable is not available for that instance(object)
b.info()
c=student("vyhjv",[45,56,67])
student.school="pqr"
c.info()
b.add(2,3)
student.add(5,7)



print("______classmethos______")
class employee:

    company="apple"

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self): 
        print(f"{self.company}'s employee {self.name} has employee id {self.id}")

    def change_company(cls,new): # it works as normal fn which take first argument as instance(cls) and change company name for that particular object
        cls.company=new

    @classmethod
    def change_cmp(cls,new): #here cls is for class , changing company value for entire class
        cls.company=new

    @classmethod              # alternative constructor bcz it takes inputs which constructor can not take. 
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1]) #It directly calls the class constructor (cls) with the extracted values from the string.
    
        #return (cls.string.split("-")[0],cls.string.split("-")[1])  it is like ywe are trying to access a class attribute named string and then apply split on it. However,
        # the attribute string is not defined in the class, and we are essentially trying to access it as if it's an attribute of the class, which will result in an AttributeError.
        
a=employee("aayushi",500)
a.show()
a.change_company("tesla")
a.show()
print(a.company)
print(employee.company,"\n")

b=employee("krutika",400)
b.show()
b.change_cmp("nestle")
b.show()
print(b.company)
print(employee.company)

str=("aayushi-300")  # if we get data in this format, we can directly pass it to the constructor. We have split strings. but splitting the string for all instances is not appropriate.  
c=employee.fromstr(str)
c.show()



print("_______decorator_______")

#Decorators are a way to extend the functionality of a function or method without modifying its source code.
#A decorator is a function that takes another function as an argument and returns a new function that modifies the 
#behavior of the original function.

def decorator(fn):
    def mfn(*arg, **arg2): #*arg allows a function to accept any number of int arguments
                           #**arg2 allows a function to accept any number of keyword arguments like dictionary,string etc.
        print("hello , you are using decorator ")
        fn(*arg, **arg2)
        print("thank you")
    return mfn

@decorator
def add(a,b):
    print(a+b)

@decorator
def hello():
  print("Hello world")

hello()
add(6,7)

import logging

logging.basicConfig(level=logging.INFO)
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    print( a + b )

result = my_function(2, 3)
print(result)









