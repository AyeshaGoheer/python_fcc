# 1. Create a variable called "sentence" and assign any sentence of your choice to it as a string.
sentence = "The quick brown fox jumps over the lazy dog."


# 2. Print the length of the "sentence" using the len() function.
print(len(sentence))


# 3. Convert the "sentence" to uppercase and print the result.
print(sentence.upper())

# 4. Check if the word "fox" is present in the "sentence" and print the result as a boolean.
if "fox" in sentence:
    print("True") 
else:
    print("False")  

# 5. Find the index of the word "brown" in the "sentence" and print the result.
abc= sentence.index("brown")
print(abc)

# 6. Create a variable called "words" and split the "sentence" into a list of words using the split() method.
words=sentence.split()

# 7. Print the list of words.
print(words)

# 8. Join the words in the "words" list using a space as the separator and assign the result to a new variable called "new_sentence".
new_sentence= " ".join(words)


# 9. Print the "new_sentence".
print(new_sentence)

# 10. Replace the word "lazy" in the "sentence" with the word "active" and print the updated sentence.
updated_sentence=sentence.replace("lazy", "active")
print(updated_sentence)
















