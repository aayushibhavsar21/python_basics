participant=['abc','pqr','xyz','mno','cde']

print(participant)
print(participant[2])
print(participant[-1],participant[-2])

participant[2]=input("enter new value:")
print(participant)

m=input("enter index you want to delete:")
val=int(m)
del participant[val]
print(participant,participant[1:4],participant[2:3],participant[:2],participant[2:],participant[-2:],participant[-1:],end="\n")

participant.sort()
print(participant)



even=[2,4,6,8,10,12,14,16,18,20]
print(even[1:len(even)-1:2]) #list[start:end:jump]
print(even[0:len(even):3]) 



Numbers = [15, 40, 50]
Numbers.append(100)
Numbers.insert(1,20)
print(Numbers)

add=[115,140]
Numbers.extend(add) # or new=Number+add
print(Numbers,len(Numbers),Numbers.index(50),end="\n")

new=[89,45,32]
bigger=[Numbers,new]
print(bigger)

Numbers.sort()
print(Numbers)
Numbers.sort(reverse=True)
print(Numbers)



lst = [i for i in range(5)]
print(lst)
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(11) if i%2==0]
print(lst)



name=["milo","sarah","bruno","anastasia","rosa"]
lst1=[n for n in name if 'o' in n ]
print(lst1)
lst2=[n for n in name if len(n)>4]
print(lst2)

new=name.copy()
new[0]="marya"
print(new)
print(name)

new=name  # here new is reference of name (not copy of name) so,if we change new then name will also change
new[0]="marya"
print(new)
print(name)