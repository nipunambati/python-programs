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

