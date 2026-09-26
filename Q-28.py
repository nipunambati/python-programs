Q-28 Find factorial of N

n = int(input("Enter N: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "is", factorial)
