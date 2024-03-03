try:
    num=int(input("enter number:"))
    print("multiplication table of ",num)
    for i in range(1,11):
       print(num,"*",i,"=",num*i)
    a=[4,6,8]
    ind=int(input("enter index:"))
    print(a[ind])
    
except ValueError:
    print("number entered is not an integer:")

except IndexError:
    print("index out of bound")

finally:
    print("final block")

#main important of block is in function. if we use try and except in function and return some value then return means termination of function
    #in this kind of situation finally is most useful to execute neccesary code in function.



print("raise - to raise custom errors")

ele=input("enter value between 5 to 9:")
if ele=="quit":
    exit 
elif int(ele)>9 or int(ele)<5:
    raise ValueError("value should be between 5 and 9")