Q-1 

name = ""
age = 
college = ""
branch = ""

print(name)
print(age)
print(college)
print(branch)



Q-2 

name = input("Enter your name:nipun ")
print("Hello,", name + "!")

Q-3 

string = "nipun"
for char in string:
    print(char)

Q-4

text = "Python is Fun!"
vowels = "aeiou"
vowel_list = [char for char in text if char in vowels]
print("Vowels found:", vowel_list)
print("Total number of vowels:", len(vowel_list))

Q-5 

s = "Count the spaces in this string."
spaces = s.count(" ")
print(spaces)

Q-6 

s = "nipun"
reversed_s = s[::-1]
print(reversed_s)

Q-7

text = "banana"
char_to_count = "a"
count = text.count(char_to_count)
print(f"The character '{char_to_count}' appears {count} times.")

Q-8

sentence = "Python is fun."
word_count = len(sentence.split())
print(word_count)

Q-9

s = "a aa aaa aa"
longest = max(s.split(), key=len)
print(longest)

Q-10

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word = "Racecar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")

Q-11

text = "nipun"

print(text.lower())
print(text.upper())
print(text.islower())
print(text.isupper())

Q-12 

name = input("Enter your name:")

print(f"Hello, {name}! Welcome!")


Q-13 





