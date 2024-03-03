list=[26,23,42,49,23,59,29,29,57,40]
#for i in range(10):
#   ele=int(input("enter number:"))
#    list.append(ele)

print(list)
mean=round((sum(list))/len(list),4)
print(mean)

list2=[]
for i in range (10):
    a=(pow(list[i]-mean,2))
    list2.append(a)

SD=round(pow(sum(list2)/10,1/2),4)
print("standar deviation:",SD)

SE=round(SD/pow(10,1/2),4)
print("standard error:",SE)

T=1.83
ME=T*SE
print("margin of erroe:",ME)

UB=round(mean+ME,2)
LB=round(mean-ME,2)
print("confidence interval: ",LB," to ",UB)
print("number of pairs:", round(UB))