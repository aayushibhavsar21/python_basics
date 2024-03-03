print("python's first program.")

x=input("enter value:")
print(x)
y=7.456
print(x,y)                  # case sensititve cann't write Y for y
print(int(y),",",float(x))

print(type(3.897))



a=True                      # for True and False first later should be capital
print(type(a))



x=4
print(x)
def fn():
    global x
    x=5                   #Changing the value of any variable inside fn makes changes only within fn, it is not applicable outside of fn.
    y=1                   #value declared in fn is only accessible within fn. 
    print("local x:",x)    
    print("hello")
print(f"global x:{x}")
fn()
print(f"global x:{x}")
#print(f"value of y:{y}")  #value is declared in fn so not accessible here 



s1,s2=input("enter any 2 strings:").split()
print(s1+s2)
print(x,"rupees")
print(str(x) +" dollars")   # print(x + "dollar") is snot executable because x and dollar have different data types.

print(s1.upper())
print(s2.lower())



s3= "I'm fine"              # string 'I'm fine' will throw error . so we can write it using eihter s3 or s4.
s4= 'I\'m fine'             # \- escape character - it changes the interpretation of characters immediately after it
s5='press "enter"'   



quantity = 3
itemno = 567
price = 49.955
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 
myorder = "I want {1} pieces of item {2} for {0} dollars."
print(myorder.format( price,quantity, itemno)) 
myorder =f"I want {quantity} pieces of item {{itemno}} for {price:.2f} dollars." #f-string
print(myorder)

print(type(f"2*30"))