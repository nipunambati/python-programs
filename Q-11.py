Q-10 Check whether a string is palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word = "Racecar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")

