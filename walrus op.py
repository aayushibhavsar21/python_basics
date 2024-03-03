#walrus oprator (:=) allows you to assign a value to a variable within an expression

a=True
# print(a=False) # error
print(a:=False)



numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())



foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)