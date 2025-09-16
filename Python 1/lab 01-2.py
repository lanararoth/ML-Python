limit = int(input("Enter a limit "))

for i in range(limit):
    age = int(input("Enter your age "))
    if(age>18):
        print(" you are eligible ")
    else:
        print(" you are not eligible ")
    