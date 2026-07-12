import pandas as pd

data = {
    'ID': [101, 102, 103],
    'Name': ['John', 'Steve', 'Mike'],
    'Marks': [85, 89, 75]
}

df = pd.DataFrame(data)

df.to_json("test_students_1.json")  # Creates whole JSON content in one line

df.to_json(
    "test_students_2.json",
    orient='records',
    indent=4
)  # Creates JSON content, with line spacing of 4 char from start of the line
