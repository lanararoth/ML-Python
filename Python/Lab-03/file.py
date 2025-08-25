file = open("out.txt","w")
file.write("hELLLOOOOO hiiiii")
file.close

file = open("out.txt")
print(file.read())
file.close()