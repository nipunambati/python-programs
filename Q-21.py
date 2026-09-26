Q-21 Find greater of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater.")
elif num2 > num1:
    print(f"{num2} is greater.")
else:
    print("Both numbers are equal.")
