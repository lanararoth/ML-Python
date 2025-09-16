file=open("inp.txt","r")
file2=open("out.txt", "w")
file2.write(file.read() + "\n")
file.close()
file2.close()
file = open("out.txt", "a")
for i in range(1, 24):
    num=str(i)+"\n"
    file.write(num)
file.close()
