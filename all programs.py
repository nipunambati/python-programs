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

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

print("\n--- Results ---")
print(f"Addition ({num1} + {num2}) = {addition}")
print(f"Subtraction ({num1} - {num2}) = {subtraction}")
print(f"Multiplication ({num1} * {num2}) = {multiplication}")
print(f"Float Division ({num1} / {num2}) = {division}")
print(f"Floor Division ({num1} // {num2}) = {floor_division}")
print(f"Modulus/Remainder ({num1} % {num2}) = {modulus}")
print(f"Exponentiation ({num1} ** {num2}) = {exponentiation}")

Q-14 

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

Q-15

eng = float(input("eng: "))
hindi = float(input("hindi: "))
maths = float(input("maths: "))
python = float(input("python: "))
sci = float(input("sci: "))

total_marks = eng + hindi + maths + python + sci
percentage = (total_marks / 500) * 100

print("\n--- Results ---")
print(f"Total Marks Obtained: {total_marks} / 500")
print(f"Percentage: {percentage:.2f}%")

Q-16 

a = 10
b = 20

print(f"The value of a is {a}")
print(f"The value of b is {b}")

temp = a
a = b
b = temp

print(f"The value after swapping of a is {a}")
print(f"The value after swapping of b is {b}")

Q-17 

total_seconds = 10000

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")

Q-18

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

Q-19

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


Q-20

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

Q-21

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater.")
elif num2 > num1:
    print(f"{num2} is greater.")
else:
    print("Both numbers are equal.")

Q-22

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

Q-23 







