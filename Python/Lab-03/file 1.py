file = open("inp.txt","w")
file.write("Helooo Hiii")
file.close()

file = open("inp.txt","r")
print(file.read())
file.close()