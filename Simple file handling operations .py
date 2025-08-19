# Open file in write mode and add text
f = open("sample.txt", "w")
f.write("Hello, this is Yash.\n")
f.close()

# Read the file
f = open("sample.txt", "r")
print("File Content:")
print(f.read())
f.close()

# Append new text
f = open("sample.txt", "a")
f.write("This is an extra line.\n")
f.close()
