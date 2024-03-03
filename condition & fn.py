print("\nconditions:")

#is and == are both comparison operators that can be used to check if two values are equal.
#The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only 
#return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

#a and b are two separate lists that have the same values, so == returns True.but a and b are not the same object in memory,so is returns False.

#in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings
#and integers, is and == will always return the same result:

a = "hello"
b = "hello"
print(a == b)  # True
print(a is b)  # True
a = 5
b = 5
print(a == b)  # True
print(a is b)  # True



x = 7
x = 5**2     # reassignment 
print ( x==25 , x==7 )
print(23 <= 10*2)
print(5*3 != 5**3)
print ( False or not True and True )   # order of execution: 1st not --> 2nd and --> 3rd or
print( 5 is 6 , 5 is not 6)            # identity operators ( is , is not )



a=10
b=25
if a>3 and b>13:
    print ("Both conditions are correct")
if a<3 or b<13:
    print ("At least one of the conditions is false")



p,q=input("enter 2 numbers:").split()
a,b=int(p),int(q)
if a>3 and b>13:
    print (".Both conditions are correct")
if a<3 or b<13:
    print (".At least one of the conditions is false")
else:
    print("---")

#if a<3 or b<13:
#   print ("At least one of the conditions is false")
#   else:
#   print("---")
# above code is not executable because else is not a part of if block else is new statement so it should not be in if block.



#def hello(a,b) this will throw error bcz we haven't defined any body body of hello fn
def hello(a,b):
    pass
#pass in above code means we will define function body later.



print("function:")
def compare1(num):
    if num > 5 :
        return "greater"
    elif num < 0 :
        return "negative"
    elif num < 5 :
        return "less"
    else :
        return "equal"

def compare2(num):     #num is a parameter
    if num > 5 :
        return "greater"
    elif num < 5 :
        return "less"
    elif num < 0 :
        return "negative"
    else :
        return "equal"
    
print(compare1(-7))     # -7 is a argument
print(compare2(-7))     # it shows the order of statements metters



print("recurssive function:")
def factorial(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial(4))



def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(7):
    print(fibonacci(i))



def avg(a=5,b=7):
    print((a+b)/2)

avg()
avg(3)
avg(b=9)
avg(1,9)
avg(b=9,a=1)



def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)



print("built-in functions")

list=[1,2,3,4,5]
print(type(4.66),int(6.8),float(6),str(590),max(60,34,68),min(26,63,79),abs(-27),sum(list), \
      sum(list,6),round(5.2135,2),round(5.32),pow(2,4),len("data science"))
