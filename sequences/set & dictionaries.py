print("__________set__________")

s={1,2,3,7,2,8,9,1}
print(s)  #Sets do not allow duplicate values.
s2={1,7,8,9}

info = {"Carla", 9, False, 7, 9}
print(info) #Sets are unordered collection of data items.
#print(info[0],info[1],info[3]) -not possible #items of set occur in random order and hence they cannot be accessed using index numbers. 
#for value in info:
 #   print(value)
info2 = {"Carla","roy","beny","jack"}

print(s.union(info),s.intersection(info),s.difference(info),s,info)
print(s.symmetric_difference(info))  #The symmetric_difference() prints only items that are not similar to both the sets.
print(s.isdisjoint(info,),s.issuperset(s2),s2.issubset(s))
#disjoint checks if items of given set are present in another set. This method returns False if items are present, else it returns True

s.update(info)
info.intersection_update(info2)
print(s,info)

print(s2,info2)
s2.add(11),info2.remove("jack")
print(s2,info2,s2.pop())
del s #entire set has been deete so can not use it now onwards.
info.clear()
print(info)

aayu={}
print(type(aayu))
aayu=set()
print(type(aayu))



print("__________dictionary__________")

#dictionary have all method sets have . likeupdate,add,del,pop,remove
dict={ 'stud1':89 , 'stud2':78 , 'stud3':47 , 'stud4':92 }
print(dict)
print(dict['stud2'])
dict['stud1']=85
print(dict)



dep_worker={'dep1':'emp1' , 'dep2':{'emp2', 'emp3'}}
print("\n",dep_worker)
print(dep_worker['dep2'])
print(dep_worker.items())
for key,value in dep_worker.items():
    print(key,"-",value)



team={}
team['pos1']={'worker1'}
team['pos2']={'worker2'}
team['pos3']={'worker3','worker4'}
team['pos4']={'worker5','worker6','worker7'}
print("\n",team)
print(team.get('pos2'))
#print(team['pos5']) this will throw error
print(team.get('pos5')) # this will return none
print(team.keys())
print(team.values())
for keys in team:
    print(team[keys])



Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna'}
Dessert = ['Pancakes', 'Ice-cream', 'Tiramisu']
Menu['meal_6']=Dessert
print("\n",Menu)  #\n - escape sequence character.

Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna', 'meal_5':'Soup'}
Price_list = {}
Price_list[Menu['meal_1']]=10
Price_list[Menu['meal_2']]=5
Price_list[Menu['meal_3']]=8
Price_list[Menu['meal_4']]=12
Price_list[Menu['meal_5']]=5
print("\n",Price_list)   #\n - escape sequence character.