def fact (num):
    if num == 0 or num ==1:
        return 1
    else:
        return num * fact(num -1)
    
num = int(input(" enter the no  "))
print(" factorial " + str (fact(num)))

num=int(input("enter the no  "))
fact=1
while(num!=0):
    fact=fact*num
    num-=1

print("factorial  "+str(fact))