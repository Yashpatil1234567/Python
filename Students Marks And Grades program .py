
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

# Taking marks of 5 subjects
marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculating total and percentage
total = sum(marks)
percentage = total / 5


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"


print("\n----- Student Result -----")
print(f"Name       : {name}")
print(f"Roll No.   : {roll}")
print(f"Marks      : {marks}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
