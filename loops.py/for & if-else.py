#space before statements in any block is called indentation
list=[]
size=int(input("enter size of index:"))
for i in range(0,size):
    ele=int(input("enter element:"))
    list.append(ele)
print(list)    



even=[2,4,6,8,10,12,14,16,18,20]
for n in even:
    print(n,end=',')

for n in range(len(even)):
    print("\n",even[n])



#odd / even
#first method to find odd /even using if else
for i in range(20):
    if i%2==0:
        print(i,"is even.")
    else:
        print(i,"is odd.")
else:
    print("out of for loop")

#second method to find odd/even using short hand if else
for i in range(20):
    print(i,"-even") if i%2==0 else print(i,"-odd")



for i in range(5):
    print(2**i,end=',')
else:
    print("___")

#if we put break statement in for loop then for break else will also not get executed. because else is in loop of for if condition get false 
   # for for then else statements will get execute.



#prime / not prime
num=int(input("enter number to check whether it is prime or not:"))
temp=0
for i in range(2,num):
    if num%i==0:
        temp=1

#first method to print prime/not prime using if else
if temp==1:
    print(num,"is not prime.")
else:
    print(num,"is prime")

#second method to print prime/not prime using short hand if else
print(num,"is not prime") if temp==1 else print(num,"is prime")



list = [*range(1,11)]
print(list)
for i in range(1,len(list),2):
    #print(i)
    print(list[i])



#counting of numbers which are greater than 40
def count(numbers):
    temp=0
    for z in numbers:
        if z>40:
            temp+=1
    return temp
print("enter ele for list:")
list=[]
for i in range(7):
    ele=int(input())
    list.append(ele)
print(count(list))



#total amout
price={ 'spaghetti':56 ,
        'lasagna':23 ,
        'hamburger':30
      } 
quantity={ 'spaghetti':6 ,
           'lasagna':3 ,
           'hamburger':5
         }
money=0
for i in quantity:
    print(i)
    money=money+(price[i]*quantity[i])
print(money)   

color=["blue","green","yellow","white","red"]
for x in color:
    print(x)
    for y in x:
        print(y)