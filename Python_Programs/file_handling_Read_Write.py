# Read/Write/Append files

file1 = open("sample.txt", "r")
content = file1.read()
print(content)  # Whole content of the file
print("==================")

with open("sample.txt", "r") as file1:
    content = file1.read()
    print(content) # Whole content of the file
print("==================")

with open("sample.txt", "r") as file1:
    line = file1.readline()
    print(line) # First line of the file
print("==================")


with open("sample.txt", "r") as file:
   lines = file.readlines() # Whole content of the file as a list, not line by line
   print(lines)
print("==================")

f1 = open("sample_file.txt", "w") # Overwrites the file if exists, if not creates one
f1.write("This is to test Python write mode.\n")
f1.write("Opened the file using write mode and adding some content to the file")
print ("File: sample_file.txt created")
f1.close()
print("==================")

with open("sample_file.txt", "a") as file:  # Extends the content of existing file
    file.write("\nNew line added")
print ("File: sample_file.txt updated")
print("==================")