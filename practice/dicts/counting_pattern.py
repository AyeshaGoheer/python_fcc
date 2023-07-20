


# counting words by entering text
print ("Enter some text:")
text = input(" ")
entered_text = text.split()
print(entered_text)


counts = dict()
for words in entered_text:
    count = counts.get(words , 0)
    counts[words] = count + 1

print (counts)



# counting by reading a file
file = open("practice/file.txt", "r")
text = file.read()
# print(text)
text_list = text.split()
# print(text_list)

counts = dict()
for words in text_list:
    count = counts.get(words , 0)
    counts[words] = count + 1

print (counts)













