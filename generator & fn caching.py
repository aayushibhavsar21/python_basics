print("________generator________")
#generators allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.
#you can create a generator by using the yield statement in a function. 
#The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested.

def my_generator():
    for i in range(50000000):
      # Complex computations
      yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in  gen:
  print(j)



print("________function caching________")

#Function caching store the results of a function call so that you can reuse the results instead of recomputing them every time
#function caching can be achieved using the functools.lru_cache decorator.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
    
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(61))
print("done for 61")