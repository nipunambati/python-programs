Q-1 Print name, age, college and branch 

name = ""
age = 
college = ""
branch = ""

print(name)
print(age)
print(college)
print(branch)

Q-2 Take name as input and greet the user

name = input("Enter your name:nipun ")
print("Hello,", name + "!")

Q-3 Take a string and print each character

string = "nipun"
for char in string:
    print(char)

Q-4 Count vowels

text = "Python is Fun!"
vowels = "aeiou"
vowel_list = [char for char in text if char in vowels]
print("Vowels found:", vowel_list)
print("Total number of vowels:", len(vowel_list))

Q-5 Count spaces

s = "Count the spaces in this string."
spaces = s.count(" ")
print(spaces)

Q-6 Reverse a string

s = "nipun"
reversed_s = s[::-1]
print(reversed_s)

Q-7 Count occurrence of a character

text = "banana"
char_to_count = "a"
count = text.count(char_to_count)
print(f"The character '{char_to_count}' appears {count} times.")

Q-8 Count words in a sentence

sentence = "Python is fun."
word_count = len(sentence.split())
print(word_count)

Q-9 Find the longest word

s = "a aa aaa aa"
longest = max(s.split(), key=len)
print(longest)

Q-10 Check whether a string is palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word = "Racecar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")

Q-11 Convert lowercase to uppercase

text = "nipun"

print(text.lower())
print(text.upper())
print(text.islower())
print(text.isupper())

Q-12 Take name as input and greet the user

name = input("Enter your name:")
print(f"Hello, {name}! Welcome!")

Q-13 Perform all arithmetic operations on two numbers

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

Q-14 Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

Q-15 Calculate total and percentage of 5 subjects

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

Q-16 Swap two numbers

a = 10
b = 20

print(f"The value of a is {a}")
print(f"The value of b is {b}")

temp = a
a = b
b = temp

print(f"The value after swapping of a is {a}")
print(f"The value after swapping of b is {b}")

Q-17 Convert seconds into hours, minutes and seconds

total_seconds = 10000

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")

Q-18 Check whether a number is positive, negative or zero

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

Q-19  Check whether a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

Q-20 Check whether a person is eligible to vote

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

Q-21 Find greater of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater.")
elif num2 > num1:
    print(f"{num2} is greater.")
else:
    print("Both numbers are equal.")

Q-22 Check whether a year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

Q-23  Print numbers 1–10

for i in range(1, 11):
    print(i)


Q-24 Print numbers 10–1

for i in range(10, 0, -1):
    print(i)


Q-25 Print multiples of 5

for i in range(5, 51, 5):
    print(i)

Q-26 Print multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

Q-27 Sum numbers 1–10

total = 0

for i in range(1, 11):
    total += i

print(total)

Q-28 Find factorial of N

n = int(input("Enter N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "is", factorial)


Q-29 Grade calculator from marks

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Grade F")

Q-30 Check whether a number lies between 10 and 50

num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("The number lies between 10 and 50")
else:
    print("The number does not lie between 10 and 50")











