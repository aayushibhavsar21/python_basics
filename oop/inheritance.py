class student:
    def __init__(self,name,id):  #Magic/Dunder Method
        self.name=name
        self.id=id

    def show(self):
        print(f"{self.name} has student id {self.id} ")

    def __len__(self):        #Magic/Dunder Method
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    #given Magic/Dunder Method are used in getter & setter file 
    def __str__(self):
        return f"The name of the employee is {self.name} str"
      
    def __repr__(self):
        return f"Employee('{self.name}')"
  
    def __call__(self):    #The call method is used to make an object callable, meaning that you can pass it as a parameter to a 
                                #function and it will be executed when the function is called.
        print("Hey I am good")


class stud_details(student):
    def __init__(self,name,id,std,div):
        super().__init__(name,id)
        self.std=std
        self.div=div
 
    def show(self):
        super().show()
        print(f"study in class {self.std} - {self.div}")

a=student("aayushi",500)
a.show()
print(len(a))
b=stud_details("krutika",404,11,"a")
b.show()



print("______multiple inheritance______")

class Employee:
  def __init__(self, cmp_name):
    self.cmp_name = cmp_name
  def show(self):
    print(f"The company name is {self.cmp_name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class person(Employee, Dancer):
  def __init__(self, dance, cmp ,name):
    self.dance = dance
    self.cmp_name = cmp
    self.name=name

o  = person("Kathak", "apple" , "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(person.mro())



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = GoldenRetriever("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())

