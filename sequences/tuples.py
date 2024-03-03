# Tuple
tuple = (1, 2, 3)
#tuple[0] = 4  # This will raise a TypeError

# List
my_list = [1, 2, 3]
my_list[0] = 4  # This is allowed

print(tuple)
print(tuple[0])

my_tuple2=(5,6,7)
new_tuple=(tuple,my_tuple2) # can also make list using 2 tuples.
print(new_tuple)



name, age = 'Peter,24'.split(',')
print(name,age)



Tuple = (0, 1, 2, 3, 21, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is at index:', res)
res = Tuple.index(2,4,9)   #index(element, start, end)
#res = Tuple.index(2,4,8)   this will throw error bcz end is 8th index so it will consider till 7th index and 2 is on 8th index.
print(res)


0
def rectangle_info(l,w):
    area=l*w,
    perimeter=2*(l+w)
    return area,perimeter   #fn can provide tuples as return value
    
print(rectangle_info(2,3))
