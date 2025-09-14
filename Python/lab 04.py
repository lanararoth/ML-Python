class Data:
    name = ""
    age = 22
    
n = int(input ("How many data do you want to store:\n"))

Datas = []

while n != 0:
    p1 = Data()
    p1.name = input("\nenter your name\n")
    p1.age = int(input("\n enter your age\n"))
    Datas.append(p1)
    n -= 1

for i,data in enumerate(Datas,1):
    print(f"\n No:{i} \n Name:{data.name} \n Age:{data.age}\n")