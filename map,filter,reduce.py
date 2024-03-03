print("______MAP______")

lt=[1,2,3,4,5,6,7]
new=list(map(lambda x : x**3,lt))
print(new)


print("______FILTER______")
def final(a):
    return a>3
lt2=list(filter(final,lt))
print(lt2)

from functools import reduce
print("______REDUCE______")
print(reduce(lambda x,y : x+y , lt)) # lt=[1+2,3,4,5,6,7] -> lt=[3+3,4,5,6,7] -> lt=[6+4,5,6,7] -> lt=[10+5,6,7].....