# Extracting data from a file

# Place below content to sample.txt
'''
Python is a high-level programing language 
which is identified for English like syntax
that increases readability. This simple and
predictable syntax structure makes Python 
the best choice for beginners as well as 
professionals. Python requires much less 
code compared to most other languages. 
Python is an interpreted language. An interpreted 
language executes code line by line at runtime.
'''

with open("sample.txt") as f1:
    data = f1.readlines()
    print(data[1])    # Display 2nd line only # Output:  “which is identified for English like syntax”
    print(data[0])    # Display 1st line only # Output:  “Python is a high-level programing language”
    print(data[-1])   # Display Last line only # Output:  “language executes code line by line at runtime.”
    print(data[3:7])  # Display from 4th line till 7th line as a list, Last Index position is not included

   # Display from 4th line till 7th line by line with extra end of line(carriage return)
    new_data = data[3:7]
    for lines in new_data:
       print(lines)

   # Display from 4th line till 7th line by line with out extra end of line due to 'end = ""' in print stmt
    new_data = data[3:7]
    for lines in new_data:
       print(lines, end = "")

    # Display data of the file from beginning till 4th line (Start position is null here, so its taken as 0)
    new_data = data[:4]
    for lines in new_data:
        print(lines, end = "")

    # Display data of the file from 6th line till end of file (End position is null here, so its taken as End of File)
    new_data = data[5:]
    for lines in new_data:
        print(lines, end = "")
