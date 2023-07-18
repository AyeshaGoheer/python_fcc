
"""
 1. Write a function called "count_vowels" that takes a string parameter and returns the count of vowels (a, e, i, o, u) in the string.
    Use a loop to iterate over each character in the string and check if it's a vowel.
    Initialize a counter variable to 0 and increment it whenever a vowel is found.
    Finally, return the counter value.
"""
def count_vowels(string):
    vowels=["a","e","i","o","u"]
    count=0
    for vowel in string:
        if vowel in vowels:
            count += 1
    return count

vowels_in_string= count_vowels("ayesha")
print(vowels_in_string)


"""
2. Write a function called "analyze_text" that takes a string parameter and performs the following tasks:
    - Print the length of the string.
    - Print the string in uppercase.
    - Print the count of vowels using the "count_vowels" function.
    - Check if the string contains the word "python" (case-insensitive) and print the result.
    - Print each word in the string using a loop.
"""

def analyze_text(string):
    print("Length of the string:" , len(string))
    print("Uppercase string: " , string.upper())
    print("Count of vowels:" , count_vowels(string))
    
    word="Python"
    if word in string:
        print("Contains 'python'?" , "True")
    else:
        print("Contains 'python'?" , "False")

    for each_word in sample_text.split():
        print(each_word)


# 3. Call the "analyze_text" function with a sample string of your choice.


sample_text = "Python is a powerful programming language. It is widely used for various applications."
analyze_text(sample_text)


