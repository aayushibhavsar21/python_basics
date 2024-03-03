list=[]
size=int(input("enter size of index:"))
x=0
while x<size:
    ele=int(input(print("enter element:")))
    list.append(ele) 
    x+=1
print(list)



x=1
print("odd numbers till 30:")
while x<30:
    print(x,end=' ')
    x+=2
else:
    print("out of while loop")

#if we put break statement in while loop then for break else will also not get executed. because else is in loop of while if condition get false 
   # for while then else statements will get execute.



nums = [1,35,12,24,31,51,70,100]
count=0
x=0
while x<len(nums):
    if nums[x]<20:
        count+=1
    x+=1    
print(count)
