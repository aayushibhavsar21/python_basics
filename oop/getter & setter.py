class myclass:
    def __init__(self,val):   #automatically invoked when you create a new instance of a class.
        self.value=val
        
    @property  #getter
    def getter(self):
        return 10*self.value
    
    @getter.setter 
    def setter(self,new_val):
        self.value=new_val/10

a=myclass(23)
print(a.value)
print(a.getter)
a.setter=450
print(a.setter)
print(a.value)



from inheritance import student

e = student("Harry",456)
print(e)
print(repr(e))
# print(e.name)
# print(len(e))
e()