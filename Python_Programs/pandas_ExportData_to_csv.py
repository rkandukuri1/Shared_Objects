import pandas as pd

data = {
    'ID': [101, 102, 103],
    'Name': ['John', 'Steve', 'Mike'],
    'Marks': [85, 89, 75]
}

df = pd.DataFrame(data)

print(df)   # Verify source data

df.to_csv("test_students1.csv", index=False)   # Creates test_students1.csv file with Comma separator

df.to_csv("test_students2.csv", sep="|", index=False) # Creates test_students2.csv file with Pipe separator
