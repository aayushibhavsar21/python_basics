#range(start,stop,step)
#      start:starting point of loop (by default = 0)
#      stop:end point of loop+1 (loop will iterate till end point-1)
#      step:increment/decrement operation (by default = +1)



print(range(10))
print(list(range(10)))
print(list(range(2,10)))
print(list(range(3,20,2)))

print(" range() function to create a list with all even numbers from 0 to 30 included.")
print(list(range(0,31,2)))



def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
#As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module
square(5)
print(square.__doc__)
