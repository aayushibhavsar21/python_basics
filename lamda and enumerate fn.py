#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
print("_____lamda_____")
x = lambda a: a + 10
print(x(5))



y = lambda a, b, c: a + b + c
print(y(5, 6, 2))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))



y = lambda a,b,c : print(a) if a>b and a>c else print(b) if b>c and b>a else print(c) 
print(y(56,34,98))



def value(fn,val):
  return 6+fn(val)

print(value(lambda b : b**b,3))



print("_____enumerate fn_____")

marks=[23,54,87,14,89,98,33,59]

for index,mark in enumerate(marks):
  print("awesome!!") if index==5 else print(mark)  

for i in enumerate(marks):
  print(i)  
# it return idex and marks as tuple if we define 2 different var for tuple(first should be index and second value at index) 
  #then it will return values seperately as above for loop