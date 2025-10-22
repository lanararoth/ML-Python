limit = int(input("Enter The limit:"))

words = []
index = []

for i in range(limit):
    word = input("Enter the words: ")
    words.append(word)

word = input("Enter search word: ")

for i , data in enumerate(words):
    if word in data:
        index.append(i)
        words [i] = "1"
    else:
        words [i] = "0"

print ("Word contaiing index are : ")
print (index)
print ("word containing index value changed: ")
print (words)
